from django import template

from app_news.forms import CommentForm

register = template.Library()


@register.inclusion_tag('app_news/comment_form.html', takes_context=True)
def comment_form(context, form: CommentForm):
    context.comment_form = form
    return context

