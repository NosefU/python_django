from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import ModelForm

from app_userauth.models import UserProfile


class UserRegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control',  'placeholder': 'Имя пользователя'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control',  'placeholder': 'Пароль'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control',  'placeholder': 'Повторите пароль'})
        remove_html_list = {
            '<ul>': '',
            '</ul>': '',
            '</li><li>': '\n• ',
            '<li>': '• ',
            '</li>': ''
        }
        for k, v in remove_html_list.items():
            self.fields['password1'].help_text = self.fields['password1'].help_text.replace(k, v)


class UserAuthForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserAuthForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control',  'placeholder': 'Имя пользователя'})
        self.fields['password'].widget.attrs.update({'class': 'form-control',  'placeholder': 'Пароль'})


class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'about', 'avatar']

    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Имя'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Фамилия'})
        self.fields['about'].widget.attrs.update({'class': 'form-control', 'placeholder': 'О себе'})
        self.fields['avatar'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Аватар'})
