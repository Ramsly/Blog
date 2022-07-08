from django import forms

from blog_app.models import News


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'text', 'author', 'slug']
        widgets = {'author': forms.HiddenInput()}


class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'text', 'author', 'slug']
        widgets = {'author': forms.HiddenInput()}

