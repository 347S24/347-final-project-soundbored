from django.db import models

class Audio(models.Model):
    title = models.CharField(max_length=255)
    audio_file = models.FileField(upload_to='audios/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
