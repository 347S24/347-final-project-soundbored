from django import forms
from .models import Audio
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class AudioForm(forms.ModelForm):
    class Meta:
        model = Audio
        fields = ['title', 'audio_file', 'image']
        
class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
