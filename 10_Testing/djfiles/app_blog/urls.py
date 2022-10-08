from django.urls import path

from app_blog.views import BlogRecordListView, BlogRecordDetailView, AddBlogRecord, BatchAddBlogRecord

urlpatterns = [
    path('', BlogRecordListView.as_view(), name='records_list'),
    path('record/<int:pk>', BlogRecordDetailView.as_view(), name='record_page'),
    path('record/add', AddBlogRecord.as_view(), name='add_record'),
    path('record/batch_add', BatchAddBlogRecord.as_view(), name='batch_add_record')
]
