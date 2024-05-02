from django import forms
from .models import Audio, SoundBoard
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class AudioForm(forms.ModelForm):
    class Meta:
        model = Audio
        fields = ['title', 'audio_file', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Title'}),
            'audio_file': forms.FileInput(attrs={'class': 'audio-button'}),
            'image': forms.FileInput(attrs={'class': 'audio-button'}),
        }


class SoundBoardForm(forms.ModelForm):
    audios = forms.ModelMultipleChoiceField(
        queryset=Audio.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = SoundBoard
        fields = ['title', 'audios']


class NewUserForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form__input', 'placeholder': 'Username'}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form__input', 'placeholder': 'Email'}))
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form__input', 'placeholder': 'Password'}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form__input', 'placeholder': 'Retype Password'}))

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class EmailForm(forms.Form):
    email = forms.EmailField(label='Enter your email')
