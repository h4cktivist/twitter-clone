from django import forms

from .models import Post


class PostCreationForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['text', 'image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        attrs = {
            'id': 'txtarea',
            'onKeyUp': 'AutoSize();',
            'style': 'height: 60px; max-height: 140px; width: 99%;',
            'maxlength': '800',
            'placeholder': 'Share something about'
        }
        self.fields['text'].widget.attrs.update(attrs)


class PostCreationFormAdaptive(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['text', 'image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        attrs = {
            'id': 'txtarea_lowsize',
            'onKeyUp': 'AutoSize();',
            'style': 'height: 60px; max-height: 140px; width: 99%;',
            'maxlength': '800',
            'placeholder': 'Share something about'
        }
        self.fields['text'].widget.attrs.update(attrs)
