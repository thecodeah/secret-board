from django import template

register = template.Library()

@register.simple_tag
def post_liked(post, user_id):
    return post.likes.filter(id = user_id).exists()