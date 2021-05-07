from django.contrib.auth.forms import UserCreationForm
from django import forms

from django.contrib.auth.models import User
from .models import Profile


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': 'Username'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Email'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Repeat password'})


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': 'Username', 'id': 'user_input'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Email', 'id': 'user_input'})


class ProfileUpdateForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput)
    bg_image = forms.ImageField(widget=forms.FileInput)

    class Meta:
        model = Profile
        fields = ['image', 'bio', 'bg_image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['bio'].widget.attrs.update({'placeholder': 'Say something about yourself', 'id': 'user_input_bio', 'maxlength': '280' })
        self.fields['image'].widget.attrs.update({'id': 'user_input_img'})
        self.fields['bg_image'].widget.attrs.update({'id': 'user_input'})
