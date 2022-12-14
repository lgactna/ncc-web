# Generated by Django 4.1.3 on 2022-12-14 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("writeups", "0002_member_profile_image_post_meta_image_tag_content_and_more")
    ]

    operations = [
        migrations.AddField(
            model_name="competition",
            name="competition_link",
            field=models.URLField(
                default="#", help_text="Link to competition website."
            ),
        ),
        migrations.AddField(
            model_name="competition",
            name="format",
            field=models.CharField(
                default="CTF",
                help_text="Competition format (CTF/RvB/etc.)",
                max_length=20,
            ),
        ),
        migrations.AddField(
            model_name="competition",
            name="registration_link",
            field=models.URLField(default="#", help_text="Registration link."),
        ),
    ]
