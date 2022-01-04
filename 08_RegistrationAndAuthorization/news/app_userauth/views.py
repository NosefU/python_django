from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import Permission
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.views import View, generic

from app_userauth.forms import NewsRegisterForm, NewsAuthForm, UserProfileForm
from app_userauth.models import UserProfile


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
            profile = UserProfile(user=user)
            profile.save()
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'app_userauth/register.html', context={'form': form})


class NewsLoginView(LoginView):
    template_name = 'app_userauth/login.html'
    authentication_form = NewsAuthForm


class NewsLogoutView(LogoutView):
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
            profile.phone = profile_form.cleaned_data['phone']
            profile.city = profile_form.cleaned_data['city']
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


class UserProfileVerify(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = "app_userauth.can_verify_userprofile"

    def get(self, request, user_id):
        profile = UserProfile.objects.get(id=user_id)
        profile.is_verified = True
        profile.save()
        return redirect(request.META.get('HTTP_REFERER', ''))
