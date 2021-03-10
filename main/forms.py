from django import forms

from .models import Post


class PostCreationForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['text', 'image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({'placeholder': 'Share something about'})
