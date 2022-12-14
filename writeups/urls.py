from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('competitions/', views.CompetitionsListView.as_view(), name='competitions'),
    path('competitions/<slug:pk>', views.CompetitionDetailView.as_view(), name='competition'),
    path('writeups/', views.WriteupsListView.as_view(), name='writeups'),
    path('writeup/<slug:pk>', views.WriteupDetailView.as_view(), name='writeup-detail'),
    path('writeup/<slug:pk>/images', views.writeup_images, name='images'),
    path('tools/', views.ToolsListView.as_view(), name='tools'),
    path('tool/<slug:pk>', views.ToolDetailView.as_view(), name='tool'),
    path('members/', views.MembersListView.as_view(), name='members'),
    path('member/<slug:pk>', views.MemberDetailView.as_view(), name='member'),
    path('tag/<slug:pk>', views.TagDetailView.as_view(), name='tag'),
    path('events/', views.events, name='events'),

]