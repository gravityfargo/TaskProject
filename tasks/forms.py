from django import forms
from .models import Tag

class CreateNewTag(forms.Form):
    tag_text = forms.CharField(label="Name", max_length=20)

class CreateNewTask(forms.Form):
    task_text = forms.CharField(label="Task Text", max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    task_tag = forms.ModelChoiceField(
        queryset=Tag.objects.order_by("date_created"),
        widget=forms.Select(attrs={'class': 'form-control'})
    )