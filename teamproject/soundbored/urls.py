from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.audio_upload_view, name='audio_upload'),
    path('', views.audio_list_view, name='audio_list'),  # Add this line
]


