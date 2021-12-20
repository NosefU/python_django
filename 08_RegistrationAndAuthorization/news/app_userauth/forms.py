from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import Form, ModelForm

from app_userauth.models import UserProfile


class NewsRegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(NewsRegisterForm, self).__init__(*args, **kwargs)
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


class NewsAuthForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(NewsAuthForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control',  'placeholder': 'Имя пользователя'})
        self.fields['password'].widget.attrs.update({'class': 'form-control',  'placeholder': 'Пароль'})


class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone', 'city', 'is_verified']

    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['phone'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Телефон'})
        self.fields['city'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Город'})
        self.fields['is_verified'].widget.attrs.update({'class': 'form-check-input'})
        self.fields['is_verified'].widget.attrs['disabled'] = True
