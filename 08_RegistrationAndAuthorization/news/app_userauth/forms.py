
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
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
