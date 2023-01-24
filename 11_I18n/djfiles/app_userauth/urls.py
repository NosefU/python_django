from django.urls import path

from app_userauth.views import UserRegisterView, UserLoginView, UserLogoutView, UserProfileEdit, UserProfileDetail

urlpatterns = [
    path('register', UserRegisterView.as_view(), name='register'),
    path('login', UserLoginView.as_view(), name='login'),
    path('logout', UserLogoutView.as_view(), name='logout'),
    path('profile/edit', UserProfileEdit.as_view(), name='user_profile_edit'),
    path('profile/<int:pk>', UserProfileDetail.as_view(), name='user_profile_detail')
]
