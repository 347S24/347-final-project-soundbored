# Generated by Django 4.2.11 on 2024-05-01 21:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('soundbored', '0015_audio_uploader'),
    ]

    operations = [
        migrations.AddField(
            model_name='soundboard',
            name='audios',
            field=models.ManyToManyField(related_name='included_in_soundboards', to='soundbored.audio'),
        ),
        migrations.AddField(
            model_name='soundboard',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='soundboards', to=settings.AUTH_USER_MODEL),
        ),
    ]