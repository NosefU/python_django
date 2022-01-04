from django import forms

from app_news.models import Comment, Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'subtitle', 'body', 'image']

    def __init__(self, *args, **kwargs):
        super(ArticleForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control',  'placeholder': 'Заголовок'})
        self.fields['subtitle'].widget.attrs.update({'class': 'form-control',  'placeholder': 'Подзаголовок'})
        self.fields['body'].widget.attrs.update({'class': 'form-control',  'placeholder': 'Текст новости'})
        self.fields['image'].widget.attrs.update({'class': 'form-control'})
        self.fields['str_tag'] = forms.CharField(max_length=100)
        self.fields['str_tag'].widget.attrs.update({'class': 'form-control',  'placeholder': 'Тег'})

    def clean_str_tag(self):
        data = self.cleaned_data['str_tag']
        return data.lower()


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['article', ]

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control',  'placeholder': 'Имя пользователя'})
        self.fields['body'].widget.attrs.update({'class': 'form-control',  'placeholder': 'Комментарий'})