from django.urls import path

from app_blog.views import BlogRecordListView

urlpatterns = [
    path('', BlogRecordListView.as_view(), name='records_list')
]
