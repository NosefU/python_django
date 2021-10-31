from django.urls import path
from . import views

urlpatterns = [
    path('', views.adv_list, name='advertisements_list'),
    path('adv_details', views.adv_details, name='advertisement_details')
]
