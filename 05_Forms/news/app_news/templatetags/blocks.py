from django import template

from app_news.forms import CommentForm

register = template.Library()


@register.inclusion_tag('app_news/navbar.html')
def navbar():
    return {}


@register.inclusion_tag('app_news/comment_form.html')
def comment_form(form: CommentForm):
    return {'comment_form': form}

