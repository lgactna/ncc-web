from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('competitions/', views.index, name='competitions'),
    path('writeups/', views.WriteupsListView.as_view(), name='writeups'),
    path('writeup/<slug:pk>', views.WriteupDetailView.as_view(), name='writeup-detail'),
    path('tools/', views.ToolsListView.as_view(), name='tools'),
    path('tool/<slug:pk>', views.ToolDetailView.as_view(), name='tool'),
    path('members/', views.MembersListView.as_view(), name='members'),
    path('events/', views.events, name='events'),
    path('tag/<slug:pk>', views.TagDetailedView.as_view(), name='tag'),
]