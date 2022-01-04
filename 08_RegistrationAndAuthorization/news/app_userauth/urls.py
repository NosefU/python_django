from django.urls import path

from app_userauth.views import NewsRegisterView, NewsLoginView, NewsLogoutView, UserProfileEdit, UserProfileDetail, \
    UserProfileVerify

urlpatterns = [
    path('register', NewsRegisterView.as_view(), name='register'),
    path('login', NewsLoginView.as_view(), name='login'),
    path('logout', NewsLogoutView.as_view(), name='logout'),
    path('profile/edit', UserProfileEdit.as_view(), name='user_profile_edit'),
    path('profile/<int:pk>', UserProfileDetail.as_view(), name='user_profile_detail'),
    path('profile/<int:user_id>/verify', UserProfileVerify.as_view(), name='user_profile_verify'),
]
