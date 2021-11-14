from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from app_news.forms import CommentForm
from app_news.models import Article, Comment


class ArticleList(ListView):
    model = Article
    context_object_name = 'article_list'
    queryset = Article.objects.all()[:20]


class ArticleDetail(View):
    def get(self, request, article_id):
        article = Article.objects.get(id=article_id)
        comment_form = CommentForm()
        comments = article.comments.all()
        context = {
            'article': article,
            'comment_form': comment_form,
            'comments': comments
        }
        return render(request, 'app_news/article_detail.html', context=context)

    def post(self, request, article_id):
        comment_form = CommentForm(request.POST)
        if not comment_form.is_valid():
            article = Article.objects.get(id=article_id)
            comment = Comment.objects.create(**comment_form.cleaned_data, article=article)
        else:
            return HttpResponseBadRequest(f'Некорректный комментарий: {comment_form.errors}')
        return HttpResponseRedirect(f'{request.path_info}#comment_{comment.id}')
