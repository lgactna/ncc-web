from django import template
register = template.Library()

@register.inclusion_tag('recent_posts.html', takes_context=True)
def show_recent_posts(context, is_authenticated):
    """
    Inclusion tag functionality associated with the columnar "recent posts"
    listing on various pages. This expects that `posts` has been included
    inside the context, which is a QuerySet of Posts.

    Note that this automatically uses is_authenticated to determine if
    private posts should be filtered, and then takes the five most recent
    posts of the remainder.
    """
    if not is_authenticated:
        recent_posts = context['posts'].filter(private=False)
    else:
        recent_posts = context['posts'].all()
    
    recent_posts = recent_posts.order_by("-post_time")[:5]

    return {'recent_posts': recent_posts}