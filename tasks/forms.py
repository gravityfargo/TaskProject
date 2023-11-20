from django.forms import TextInput
from bootstrap_datepicker_plus.widgets import DatePickerInput
from django import forms
from .models import Tag, Task


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["title", "color"]
        exclude = ("user",)
        widgets = {"color": TextInput(attrs={"type": "color"})}


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "tag", "due"]
        exclude = ("user",)
        widgets = {"due": DatePickerInput()}
