from django.forms import ModelForm
from .models import Profile


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ["dashboard_modules", "task_sort_order", "show_api_endpoints"]
        exclude = ("user",)