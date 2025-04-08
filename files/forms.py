from django import forms
from django.forms import ModelForm
from .models import File

class UploadForm(ModelForm):
    class Meta:
        model = File
        fields = ['name', 'file_type', 'file']  # Include file_type here
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'filename'}),
            'file_type': forms.TextInput(attrs={'placeholder': 'file type'})  # Optional: Add a placeholder for file_type
        }
