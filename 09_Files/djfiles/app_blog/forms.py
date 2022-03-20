from django.forms import ModelForm, CharField, ImageField


class BlogRecordForm(ModelForm):
    title = CharField(max_length=200)
    body = CharField(required=True)
    images = ImageField(allow_empty_file=True)

    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Заголовок'})
        self.fields['body'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Текст'})
        self.fields['images'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Изображение'})