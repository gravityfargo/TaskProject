from django.forms import TextInput
from bootstrap_datepicker_plus.widgets import DatePickerInput
from django.forms import ModelForm
from .models import Tag, Task


class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = ["title", "color"]
        exclude = ("user",)
        widgets = {"color": TextInput(attrs={"type": "color"})}


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "tag", "due"]
        exclude = ("user",)
        widgets = {"due": DatePickerInput()}
