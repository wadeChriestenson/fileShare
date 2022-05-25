from django import forms
from .models import userFiles


class FileForm(forms.ModelForm):
    class Meta:
        model = userFiles
        fields = ['file', 'file_name', 'desc', 'user']
        labels = {'file': '', 'file_name': 'Title', 'desc': 'Description', 'user': 'User'}
