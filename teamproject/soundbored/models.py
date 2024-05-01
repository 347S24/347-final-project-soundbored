from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User


class Audio(models.Model):
    title = models.CharField(max_length=255)
    audio_file = models.FileField(
        upload_to='audios/', validators=[FileExtensionValidator(allowed_extensions=['mp3'])])
    image = models.ImageField(
        upload_to='images/', default='images/defaultpic.png')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    favorites = models.ManyToManyField(User, related_name='favorite_audios')
    uploader = models.ForeignKey(
        User, null=True, on_delete=models.CASCADE, related_name='uploaded_audios')


class SoundBoard(models.Model):
    title = models.CharField(max_length=255)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='soundboard')
    audios = models.ManyToManyField(Audio, related_name='audios')
