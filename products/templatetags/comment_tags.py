from django import template

register = template.Library()

@register.filter
def only_active_comment(comment):
    return comment.filter(active=True) # comment.exclude(active=False)