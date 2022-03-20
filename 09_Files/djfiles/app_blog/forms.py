from django.forms import Form, CharField, ImageField, ClearableFileInput, Textarea


class BlogRecordForm(Form):
    title = CharField(max_length=200)
    body = CharField(required=True, widget=Textarea)
    images = ImageField(allow_empty_file=True, widget=ClearableFileInput(attrs={'multiple': True}))

    def __init__(self, *args, **kwargs):
        super(Form, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Заголовок'})
        self.fields['body'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Текст'})
        self.fields['images'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Изображения'})
