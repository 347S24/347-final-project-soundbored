from django.db import models

class Audio(models.Model):
    title = models.CharField(max_length=255)
    audio_file = models.FileField(upload_to='audios/')
    image = models.ImageField(upload_to='images/', default='images/defaultpic.jpeg')
    uploaded_at = models.DateTimeField(auto_now_add=True)
