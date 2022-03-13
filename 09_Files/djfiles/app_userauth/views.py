from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.views import View, generic

from app_userauth.forms import UserRegisterForm, UserAuthForm, UserProfileForm
from app_userauth.models import UserProfile


class UserRegisterView(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'app_userauth/register.html', context={'form': form})

    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            profile = UserProfile(user=user)
            profile.save()
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'app_userauth/register.html', context={'form': form})


class UserLoginView(LoginView):
    template_name = 'app_userauth/login.html'
    authentication_form = UserAuthForm


class UserLogoutView(LogoutView):
    next_page = '/'


class UserProfileEdit(LoginRequiredMixin, View):
    def get(self, request):
        profile = UserProfile.objects.get(id=request.user.id)
        profile_form = UserProfileForm(instance=profile)
        return render(
            request,
            'app_userauth/userprofile_edit.html',
            context={'profile': profile_form, 'profile_is_saved': False}
        )

    def post(self, request):
        profile_form = UserProfileForm(request.POST)
        if profile_form.is_valid():
            profile = UserProfile.objects.get(user=request.user)
            profile.first_name = profile_form.cleaned_data['first_name']
            profile.last_name = profile_form.cleaned_data['last_name']
            profile.about = profile_form.cleaned_data['about']
            profile.save()
            profile_form = UserProfileForm(instance=profile)
            return render(
                request,
                'app_userauth/userprofile_edit.html',
                context={'profile': profile_form, 'profile_is_saved': True}
            )
        else:
            return render(
                request,
                'app_userauth/userprofile_edit.html',
                context={'profile': profile_form, 'profile_is_saved': False}
            )


class UserProfileDetail(generic.DetailView):
    model = UserProfile

