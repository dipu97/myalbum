
from django import forms
from .models import album
from django.forms import ModelForm

class AlbumForm(forms.ModelForm):
    class Meta:
        model=album
        fields=['title','description','image']