from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.audio_upload_view, name='audio_upload'),
    path('', views.audio_list_view, name='audio_list'),
    path('delete/<int:audio_id>/', views.delete_audio, name='delete_audio'),
    path('favorite/<int:audio_id>/', views.add_favorite, name='add_favorite'),


]


