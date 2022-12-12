from django.shortcuts import render
from .models import Post, Member, Competition, Placement, Tool, Tag
from django.views import generic
from django.http import Http404

def index(request):
    """View function for home page of site."""

    # Get 6 most recent posts by date
    recent_posts = Post.objects.order_by("-post_time")[:6]

    context = {
        'recent_posts': recent_posts
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

class CompetitionsListView(generic.ListView):
    model = Competition
    # TODO: standardize posts vs. writeups one day lol
    context_object_name = 'competitions'

class WriteupsListView(generic.ListView):
    model = Post
    # TODO: standardize posts vs. writeups one day lol
    context_object_name = 'posts'

class WriteupDetailView(generic.DetailView):
    model = Post
    context_object_name = 'writeup'

class ToolsListView(generic.ListView):
    model = Tool
    context_object_name = 'tools'

class ToolDetailView(generic.DetailView):
    model = Tool
    context_object_name = 'tool'

class MembersListView(generic.ListView):
    # Will be necessary to split things out into groups
    # in the future, but I think this is fine for now
    model = Member
    context_object_name = 'members'

class MemberDetailView(generic.DetailView):
    # Will be necessary to split things out into groups
    # in the future, but I think this is fine for now
    model = Member
    context_object_name = 'member'

def events(request):
    """View function for the events page."""

    # Not quite sure what the best way to handle this is

    return render(request, 'events.html')

class TagDetailedView(generic.DetailView):
    # Will be necessary to split things out into groups
    # in the future, but I think this is fine for now
    model = Tag
    context_object_name = 'tag'