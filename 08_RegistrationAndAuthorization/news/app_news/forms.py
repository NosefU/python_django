from django import forms

from app_news.models import Comment, Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ArticleForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control',  'placeholder': 'Заголовок'})
        self.fields['subtitle'].widget.attrs.update({'class': 'form-control',  'placeholder': 'Подзаголовок'})
        self.fields['body'].widget.attrs.update({'class': 'form-control',  'placeholder': 'Текст новости'})
        self.fields['image'].widget.attrs.update({'class': 'form-control'})


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['article', ]

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control',  'placeholder': 'Имя пользователя'})
        self.fields['body'].widget.attrs.update({'class': 'form-control',  'placeholder': 'Комментарий'})