from django.contrib import admin
from django.contrib.auth.models import User
from django.db.utils import IntegrityError

# Users
try:
    user = User.objects.create_user(
        'Daniel', 'email@example.com', 'Password123')
    user.save()
    user = User.objects.create_user(
        'Dylan', 'email@example.com', 'Password123')
    user.save()
    user = User.objects.create_user(
        'Mateen', 'email@example.com', 'Password123')
    user.save()
except IntegrityError:
    print("Username is already taken. Please choose a different username.")
