from django.urls import path

from advertisements_app.views import AdvertisementsListView, AdvertisementsDetailView

urlpatterns = [
    path('advertisements', AdvertisementsListView.as_view(), name='advertisements_list'),
    path('advertisements/<int:pk>', AdvertisementsDetailView.as_view(), name='advertisements_detail'),
]
