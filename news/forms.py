from .models import Texts
from .models import Comments
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class TextsForm(ModelForm):
    class Meta:
        model = Texts
        fields = ['title', 'anons', 'f_text', 'date']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название статьи'
            }),
            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс'

            }),
            "f_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Cтатья'
            })

        }


class CommentsForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['kom_text']

        widgets = {
            "kom_text": Textarea(attrs={
                'class': 'btn btn-outline-light me-2 btn btn-lg btn-light fw-bold border-white bg-white',
                'placeholder': 'Текст'
            }),

        }

