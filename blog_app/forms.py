from django import forms

from blog_app.models import Comments


class LeftCommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ("user", "blog", "comment", )
        widgets = {"user": forms.HiddenInput(), "blog": forms.HiddenInput()}



