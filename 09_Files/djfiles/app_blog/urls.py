from django.urls import path

from app_blog.views import BlogRecordListView, BlogRecordDetailView

urlpatterns = [
    path('', BlogRecordListView.as_view(), name='records_list'),
    path('record/<int:pk>', BlogRecordDetailView.as_view(), name='record_page')
]
