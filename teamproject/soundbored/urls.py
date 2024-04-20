from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('upload/', views.audio_upload_view, name='audio_upload'),
    path('', views.audio_list_view, name='audio_list'),
    path('delete/<int:audio_id>/', views.delete_audio, name='delete_audio'),
    path('favorite/<int:audio_id>/', views.toggle_favorite, name='toggle_favorite'),
    path('favorites/', views.list_favorites, name='list_favorites'),
    path('soundboard/', views.soundboard_view, name='soundboard_view'),
    (path('register/', views.register_view, name='register'))
]
