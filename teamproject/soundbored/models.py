from django.db import models
from django.core.validators import FileExtensionValidator

class Audio(models.Model):
    title = models.CharField(max_length=255)
    audio_file = models.FileField(upload_to='audios/', validators=[FileExtensionValidator(allowed_extensions=['mp3'])])
    image = models.ImageField(upload_to='images/', default='images/defaultpic.jpeg')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    is_favorite = models.BooleanField(default=False)

class SoundBoard(models.Model):
    title = models.CharField(max_length=255)