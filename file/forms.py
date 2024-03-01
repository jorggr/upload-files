from django import forms
from .models import FileData


class FileForm(forms.ModelForm):
    class Meta:
        model = FileData
        exclude = ["uploaded_at"]
