from django.conf.urls.static import static
from django.urls import path
from app_news.views import ArticleList, ArticleDetail
from news import settings

urlpatterns = [
    path('', ArticleList.as_view(), name='article_list'),
    path('article/<int:article_id>', ArticleDetail.as_view(), name='article_detail'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
