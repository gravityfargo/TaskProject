from django.forms import TextInput, CharField
from django import forms
from .models import Tag

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['title', 'color']
        exclude = ('user',)
        widgets = {
            "color": TextInput(attrs={"type": "color"})
        }
