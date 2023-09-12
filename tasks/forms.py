from django import forms
from .models import Tag

class CreateNewTag(forms.Form):
    tag_text = forms.CharField(label="Name", max_length=20)

class CreateNewTask(forms.Form):
    task_text = forms.CharField(label="Task Text", max_length=50)
    task_tag = forms.ModelChoiceField(queryset=Tag.objects.order_by("date_created"))

# date_created = forms.DateField()
# date_due = forms.DateField()