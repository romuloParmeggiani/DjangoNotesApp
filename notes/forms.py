from django import forms
from django.core.exceptions import ValidationError

from .models import Notes


class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ('title', 'text')
        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control my-5"}),
            'text': forms.Textarea(attrs={"class": "form-control my-5"})
        }
        labels = {
            'text': 'Write down your notes here:'
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if 'Django' not in title:
            raise ValidationError('App only supports notes about Django')
        return title
