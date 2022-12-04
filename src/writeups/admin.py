from django.contrib import admin
from .models import Post, Member, Competition, Placement, Tool, Tag

# Register your models here.
admin.site.register(Post)
admin.site.register(Member)
admin.site.register(Competition)
admin.site.register(Placement)
admin.site.register(Tool)
admin.site.register(Tag)