from django import forms
from .models import userFiles


class FileForm(forms.ModelForm):
    class Meta:
        model = userFiles
        fields = ['file_name','file', 'user']
        labels = {'file_name': 'Title','file': '', 'user': 'User'}