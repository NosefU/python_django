from django.forms import Form, CharField, ImageField
from django_summernote.widgets import SummernoteWidget


class BlogRecordForm(Form):
    title = CharField(max_length=200)
    body = CharField(required=True, widget=SummernoteWidget())
    cover = ImageField(allow_empty_file=True)

    def __init__(self, *args, **kwargs):
        super(Form, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Заголовок'})
        self.fields['cover'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Обложка'})
        self.fields['body'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Текст'})

