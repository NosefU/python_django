from django.conf.urls.static import static
from django.urls import path
from app_news.views import ArticleList, ArticleDetail, AddArticle, EditArticle, NewsLoginView, NewsLogoutView
from news import settings

urlpatterns = [
    path('', ArticleList.as_view(), name='article_list'),
    path('article/<int:article_id>', ArticleDetail.as_view(), name='article_detail'),
    path('article/add', AddArticle.as_view(), name='add_article'),
    path('article/<int:article_id>/edit', EditArticle.as_view(), name='edit_article'),
    path('login', NewsLoginView.as_view(), name='login'),
    path('logout', NewsLogoutView.as_view(), name='logout'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
