"""
See ncc-web.vpp for more.
You can open it in Visual Paradigm.
"""
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.validators import RegexValidator, MinLengthValidator, MinValueValidator
from tinymce import models as tinymce_models


class Post(models.Model):
    """
    Represents an arbitrary post.
    """

    # Order by post time, newest to oldest
    ordering = ["-post_time"]

    # Slugs are letters, numbers, underscores, or hyphens (only).
    # By default, the length limit is 50.
    vanity_url = models.SlugField(
        verbose_name="Vanity URL",
        help_text="The vanity URL (writeups/...). Use dashes to separate words.",
        primary_key=True,
    )
    post_time = models.DateTimeField(
        verbose_name="Post time", help_text="Date of initial posting."
    )
    update_time = models.DateTimeField(
        verbose_name="Update time",
        help_text="If updated, date of update. Can be empty.",
        blank=True,
        null=True,
    )

    meta_lead = models.CharField(
        verbose_name="Meta lead text",
        help_text=(
            "The lead text shown in writeup previews and on social media (via the"
            " meta-description). Max of 150 characters."
        ),
        max_length=150,
    )
    meta_image = models.ImageField(upload_to="post-banners", blank=True, null=True)

    title = models.CharField(
        verbose_name="Post title",
        help_text=(
            "The post title; also used as the meta-title and the page title (with '|"
            " Nevada Cyber Club appended'). Max of 55 characters."
        ),
        max_length=55,
    )

    # https://django-tinymce.readthedocs.io/en/latest/usage.html#the-htmlfield-model-field-type
    # It's basically a glorified TextField.
    content = tinymce_models.HTMLField(
        verbose_name="Post content",
        help_text="A TinyMCE-driven field for the post content.",
    )

    # I don't ever see us deleting users, but I'm making the
    # judgement that we won't delete posts as well if this happens.
    # Instead, replace it with some text like "(deleted user)" or
    # "(anonymous)".
    author = models.ForeignKey(
        "Member", on_delete=models.SET_NULL, blank=True, null=True, related_name="posts"
    )
    # Same with competitions.
    competition = models.ForeignKey(
        "Competition",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="posts",
    )
    tags = models.ManyToManyField(
        "Tag", related_name="posts", blank=True  # use tags.posts.all(), for example
    )
    tools = models.ManyToManyField("Tool", related_name="posts", blank=True)

    def get_absolute_url(self):
        """
        Returns the url for this post.

        If a vanity URL is used, this is the URL returned.
        Else, returns the internal numeric ID.
        """
        return reverse("writeup-detail", args=[str(self.vanity_url)])

    def __str__(self):
        """
        String representing the post.

        :return: The post title.
        """
        return self.title


class Member(models.Model):
    # https://docs.djangoproject.com/en/dev/topics/auth/customizing/#extending-the-existing-user-model
    # The username, first_name, last_name, and groups fields are accessible through the .user attribute.
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    display_name = models.SlugField(
        verbose_name="Display name",
        help_text=(
            "Display name used in your URL and in post authoring (if necessary). 35"
            " characters max."
        ),
        max_length=35,
        unique=True,
        primary_key=True,
    )
    profile_image = models.ImageField(upload_to="profiles", blank=True, null=True)

    title = models.CharField(
        verbose_name="Title",
        help_text="Special title (e.g. President, Vice President, etc.).",
        max_length=35,
        default="",
        blank=True,
    )

    use_display_name_in_posts = models.BooleanField(
        verbose_name="Use display name in posts",
        help_text=(
            "Whether to use the display name or your full name as the post author."
        ),
    )

    content = tinymce_models.HTMLField(
        verbose_name="Profile content",
        help_text="A TinyMCE-driven field for the profile content.",
        blank=True,
        null=True,
    )

    meta_lead = models.CharField(
        verbose_name="Meta lead text",
        help_text=(
            "The lead text shown on social media (via the meta-description). Max of 150"
            " characters."
        ),
        max_length=150,
    )

    discord_tag = models.CharField(
        verbose_name="Discord tag",
        help_text="Discord tag (with discriminator).",
        max_length=50,
        blank=True,
        null=True,
    )

    def get_absolute_url(self):
        """
        Returns the url for this member.
        """
        return reverse("member", args=[str(self.display_name)])

    def __str__(self):
        if self.user.get_full_name():
            return f"{self.user.get_full_name()} ({self.display_name})"
        else:
            return f"<no name> ({self.display_name})"


class Competition(models.Model):
    # Order by start date, newest to oldest.
    ordering = ["-start_date"]

    vanity_url = models.SlugField(
        verbose_name="Vanity URL",
        help_text="The vanity URL (competition/...). Use dashes to separate words.",
        primary_key=True,
    )
    name = models.CharField(
        verbose_name="Competition name",
        help_text="The full name of the competition. 100 chars or less (enforced).",
        max_length=100,
    )
    start_date = models.DateField(
        verbose_name="Start date",
        help_text="Start date of (actual) competition.",
        blank=True,
        null=True,
    )
    end_date = models.DateField(
        verbose_name="Start date",
        help_text="End date of (actual) competition.",
        blank=True,
        null=True,
    )

    COMPETITION_TYPE = (("i", "Individual"), ("t", "Team"))

    type = models.CharField(
        help_text="Competition type (individual/team/etc.)",
        max_length=1,
        choices=COMPETITION_TYPE,
        blank=True,
        default="i",
    )

    format = models.CharField(
        help_text="Competition format (CTF/RvB/etc.)", default="CTF", max_length=20
    )

    registration_link = models.URLField(help_text="Registration link.", default="")
    competition_link = models.URLField(
        help_text="Link to competition website.", default=""
    )

    hex_validation = RegexValidator(
        r"^[0-9a-fA-F]*$", "Only valid hex characters allowed."
    )
    length_validation = MinLengthValidator(
        6, message="Hex values must be exactly 6 in length."
    )
    theme_color = models.CharField(
        max_length=6,
        help_text=(
            "The background color used for this competition. Enter as 6 hex characters."
            " Please make sure there's sufficient contrast!"
        ),
        validators=[hex_validation, length_validation],
        default="002E62",  # Navy blue used throughout the website
    )
    meta_lead = models.CharField(
        verbose_name="Meta lead text",
        help_text=(
            "The lead text shown in writeup previews and on social media (via the"
            " meta-description). Max of 150 characters."
        ),
        max_length=150,
    )
    content = tinymce_models.HTMLField(
        verbose_name="Page content",
        help_text="A TinyMCE-driven field for the post content/body copy.",
    )

    def get_absolute_url(self):
        """
        Returns the url for this tag.
        """
        return reverse("competition", args=[str(self.vanity_url)])

    def __str__(self):
        """
        String representing the competition.

        :return: The competition title.
        """
        return self.name


class Placement(models.Model):
    competition = models.ForeignKey(
        "Competition", on_delete=models.CASCADE, related_name="placements"
    )
    member = models.ForeignKey(
        "Member",
        on_delete=models.SET_NULL,
        related_name="placements",
        null=True,
        blank=True,
    )

    positive_validation = MinValueValidator(1, message="Placement must be positive!")
    rank = models.IntegerField(
        verbose_name="Placement",
        help_text=(
            "This member/team's numerical placement. Can be blank if the competition"
            " hasn't happened yet."
        ),
        blank=True,
        validators=[positive_validation],
    )
    team_name = models.CharField(
        verbose_name="Team name",
        help_text=(
            "This team's name. It only serves a vanity purpose and has no functional"
            " relationships."
        ),
        max_length=35,
        null=True,
        blank=True,
    )

    def __str__(self):
        """
        String representing placement.
        """
        return (
            f"{self.member.user.get_full_name()} - rank {self.rank} in"
            f" {self.competition}"
        )


class Tool(models.Model):
    vanity_url = models.SlugField(
        verbose_name="Vanity URL",
        help_text="The vanity URL (tool/...). Use dashes to separate words.",
        primary_key=True,
    )
    name = models.CharField(
        verbose_name="Tool name",
        help_text="Name of the tool. 50 chars max.",
        max_length=50,
    )
    image = models.ImageField(upload_to="tool-images", blank=True, null=True)
    content = tinymce_models.HTMLField(
        verbose_name="Page content",
        help_text="A TinyMCE-driven field for the tool's page content.",
    )
    meta_lead = models.CharField(
        verbose_name="Meta lead text",
        help_text=(
            "The lead text shown in writeup previews and on social media (via the"
            " meta-description). Max of 150 characters."
        ),
        max_length=150,
    )
    tags = models.ManyToManyField(
        "Tag", related_name="tools"  # use tool.tags.all(), for example
    )

    def get_absolute_url(self):
        """
        Returns the url for this tag.
        """
        return reverse("tool", args=[str(self.vanity_url)])

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.SlugField(
        verbose_name="Tag name",
        help_text="The name used for this tag. 20 characters max.",
        primary_key=True,
        max_length=20,
    )
    content = tinymce_models.HTMLField(
        verbose_name="Page content",
        help_text="A TinyMCE-driven field for the tag's page content.",
    )

    hex_validation = RegexValidator(
        r"^[0-9a-fA-F]*$", "Only valid hex characters allowed."
    )
    length_validation = MinLengthValidator(
        6, message="Hex values must be exactly 6 in length."
    )
    theme_color = models.CharField(
        max_length=6,
        help_text=(
            "The background color used for this competition. Enter as 6 hex characters."
            " Please make sure there's sufficient contrast!"
        ),
        validators=[hex_validation, length_validation],
        default="002E62",  # Navy blue used throughout the website
    )

    def get_absolute_url(self):
        """
        Returns the url for this tag.
        """
        return reverse("tag", args=[str(self.name)])

    def __str__(self):
        return self.name
