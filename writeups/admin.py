from django.contrib import admin
from .models import Post, Member, Competition, Placement, Tool, Tag, HomepageHero

# Default registrations
# admin.site.register(Post)
admin.site.register(Member)
admin.site.register(Competition)
admin.site.register(Placement)
admin.site.register(Tool)
admin.site.register(Tag)
admin.site.register(HomepageHero)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'competition', 'post_time', 'private')

# Register the admin class with the associated model
admin.site.register(Post, PostAdmin)