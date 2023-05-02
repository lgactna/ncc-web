from django.shortcuts import render
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404, HttpResponseRedirect, JsonResponse
from django.contrib.auth.mixins import AccessMixin
from django.contrib.auth.models import Group
from django.conf import settings
from django.core.files.storage import default_storage

from .models import Post, Member, Competition, Placement, Tool, Tag, HomepageHero

from uuid import uuid4
import datetime

class PostContextMixin():
    """
    Adds the context `posts`, a QuerySet of all posts associated
    with the current object.

    Should be used in detail views for which `posts` is a valid
    related name for that model.
    """
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        self.object = self.get_object()

        context['posts'] = self.object.posts.all()
        return context

def index(request):
    """View function for home page of site."""

    # Get active heroes
    heroes = HomepageHero.objects.filter(is_active=True)

    posts = Post.objects.all()

    context = {
        "heroes": heroes,
        "posts": posts,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, "index.html", context=context)


def tinymce_upload(request):
    file = request.FILES.get('file')
    filename = f"tinymce/{uuid4()}/{str(file)}"
    with default_storage.open(filename, "wb") as f:
        f.write(file.read())

    return JsonResponse({"location": f"{settings.MEDIA_URL}{filename}"})


class CompetitionsListView(generic.ListView):
    model = Competition
    context_object_name = "competitions"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Upcoming competitions are those that haven't started yet.
        context['upcoming_competitions'] = Competition.objects.filter(start_date__gt=datetime.datetime.today()).order_by("-start_date")

        # Ongoing competitions are those that have started but haven't
        # had a placement punched in yet
        context['ongoing_competitions'] = Competition.objects.filter(start_date__lte=datetime.datetime.today(), placements=None).order_by("-start_date")

        # Completed competitions are those that have started and have a
        # placement punched in.
        context['completed_competitions'] = Competition.objects.filter(start_date__lte=datetime.datetime.today()).exclude(placements=None).order_by("-start_date")

        return context


class CompetitionDetailView(PostContextMixin, generic.DetailView):
    model = Competition
    context_object_name = "competition"


class WriteupsListView(generic.ListView):
    model = Post
    # TODO: standardize posts vs. writeups one day lol
    context_object_name = "posts"

    # Add in "core" tags
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        core_tags = Tag.objects.filter(display_as_main_category=True)

        context['core_tags'] = core_tags

        return context


class WriteupDetailView(AccessMixin, generic.DetailView):
    model = Post
    context_object_name = "writeup"

    # For private posts, require the user to login.
    # The abstract AccessMixin is just used for self.handle_no_permission().
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if not request.user.is_authenticated and self.object.private:
            return self.handle_no_permission()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


@csrf_exempt
def writeup_images(request, pk: str = None):
    print("test")
    pass


class ToolsListView(generic.ListView):
    model = Tool
    context_object_name = "tools"


class ToolDetailView(PostContextMixin, generic.DetailView):
    model = Tool
    context_object_name = "tool"


class MembersListView(generic.ListView):
    # Will be necessary to split things out into groups
    # in the future, but I think this is fine for now
    model = Member
    context_object_name = "members"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Special filtering against the hardcoded Executive group
        exec_group = Group.objects.filter(name="Executive")
        all_other_groups = Group.objects.exclude(name="Executive")

        context['exec_group'] = exec_group
        context['all_other_groups'] = all_other_groups

        return context

class MemberDetailView(PostContextMixin, generic.DetailView):
    # Will be necessary to split things out into groups
    # in the future, but I think this is fine for now
    model = Member
    context_object_name = "member"

class TagDetailView(PostContextMixin, generic.DetailView):
    # Will be necessary to split things out into groups
    # in the future, but I think this is fine for now
    model = Tag
    context_object_name = "tag"


def events(request):
    """View function for the events page."""

    # Not quite sure what the best way to handle this is
    return render(request, "events.html")
