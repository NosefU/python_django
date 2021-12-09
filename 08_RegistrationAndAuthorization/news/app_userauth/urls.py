from django.urls import path

from app_userauth.views import NewsRegisterView, NewsLoginView, NewsLogoutView

urlpatterns = [
    path('register', NewsRegisterView.as_view(), name='register'),
    path('login', NewsLoginView.as_view(), name='login'),
    path('logout', NewsLogoutView.as_view(), name='logout'),
]
