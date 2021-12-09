from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View

from app_userauth.forms import RegisterForm


class RegisterView(View):
    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'app_userauth/register.html', context={'form': form})

    def get(self, request):
        form = RegisterForm()
        return render(request, 'app_userauth/register.html', context={'form': form})
