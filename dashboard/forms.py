from django.forms import ModelForm, CheckboxSelectMultiple
from .models import Profile
from tasks.models import Tag


class ProfileForm(ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user", None)
        super(ProfileForm, self).__init__(*args, **kwargs)
        username_from_create_view = kwargs.get("instance")
        # username passed from createview
        if username_from_create_view:
            self.fields["tags"].queryset = Tag.objects.filter(
                user=kwargs["instance"].user
            )
        else:
            # username passed from updateview
            self.fields["tags"].queryset = Tag.objects.filter(user=self.user)
            
        self.fields['tags'].required = False
    class Meta:
        model = Profile
        fields = ["dashboard_modules", "task_sort_order", "show_api_endpoints", "tags"]
        exclude = ("user",)
        widgets = {
            "dashboard_modules": CheckboxSelectMultiple(),
            "task_sort_order": CheckboxSelectMultiple(),
            "tags": CheckboxSelectMultiple(),
                   }