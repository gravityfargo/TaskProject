from django import forms

class CreateNewTag(forms.Form):
    tag_text = forms.CharField(label="Name", max_length=20)