from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("competitions/", views.CompetitionsListView.as_view(), name="competitions"),
    path("competitions/<slug:vanity_url>", views.CompetitionDetailView.as_view(), name="competition",),
    path("competitions/<slug:competition>/<slug:vanity_url>", views.WriteupDetailView.as_view(), name="writeup-detail"),
    path("writeups/", views.WriteupsListView.as_view(), name="writeups"),
    path("tools/", views.ToolsListView.as_view(), name="tools"),
    path("tool/<slug:vanity_url>", views.ToolDetailView.as_view(), name="tool"),
    path("members/", views.MembersListView.as_view(), name="members"),
    path("member/<slug:vanity_url>", views.MemberDetailView.as_view(), name="member"),
    path("tag/<slug:vanity_url>", views.TagDetailView.as_view(), name="tag"),
    path("events/", views.events, name="events"),
    path("tinymce-upload/", views.tinymce_upload)
]
