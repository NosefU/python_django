from django.conf.urls.static import static
from django.urls import path
from app_news.views import ArticleList, ArticleDetail, AddArticle, EditArticle, UnpublishedArticleList, PublishArticle, \
    CancelPublishingArticle
from news import settings

urlpatterns = [
    path('', ArticleList.as_view(), name='article_list'),
    path('moderate', UnpublishedArticleList.as_view(), name='unpublished_article_list'),
    path('article/<int:article_id>', ArticleDetail.as_view(), name='article_detail'),
    path('article/add', AddArticle.as_view(), name='add_article'),
    path('article/<int:article_id>/edit', EditArticle.as_view(), name='edit_article'),
    path('article/<int:article_id>/publish', PublishArticle.as_view(), name='publish_article'),
    path('article/<int:article_id>/cancel_publishing', CancelPublishingArticle.as_view(), name='cancel_publishing_article'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
