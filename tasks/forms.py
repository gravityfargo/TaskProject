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
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user", None)
        super(TaskForm, self).__init__(*args, **kwargs)
        username_from_create_view = kwargs.get("instance")
        # username passed from createview
        if username_from_create_view:
            self.fields["tag"].queryset = Tag.objects.filter(
                user=kwargs["instance"].user
            )
        else:
            # username passed from updateview
            self.fields["tag"].queryset = Tag.objects.filter(user=self.user)

    class Meta:
        model = Task
        fields = ["title", "description", "tag", "due"]
        exclude = ("user",)
        widgets = {"due": DatePickerInput()}
