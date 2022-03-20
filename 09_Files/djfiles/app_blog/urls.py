from django.urls import path

from app_blog.views import BlogRecordListView, BlogRecordDetailView, AddBlogRecord

urlpatterns = [
    path('', BlogRecordListView.as_view(), name='records_list'),
    path('record/<int:pk>', BlogRecordDetailView.as_view(), name='record_page'),
    path('record/add', AddBlogRecord.as_view(), name='add_record')
]
