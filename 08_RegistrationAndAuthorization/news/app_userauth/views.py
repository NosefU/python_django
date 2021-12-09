from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.views import View

from app_userauth.forms import NewsRegisterForm, NewsAuthForm


class NewsRegisterView(View):
    def get(self, request):
        form = NewsRegisterForm()
        return render(request, 'app_userauth/register.html', context={'form': form})

    def post(self, request):
        form = NewsRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'app_userauth/register.html', context={'form': form})


class NewsLoginView(LoginView):
    template_name = 'app_userauth/login.html'
    authentication_form = NewsAuthForm


class NewsLogoutView(LogoutView):
    next_page = '/'

