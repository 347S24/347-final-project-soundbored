from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import path
from .views import ResetPasswordView

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('upload/', views.audio_upload_view, name='audio_upload'),
    path('', views.audio_list_view, name='audio_list'),
    path('delete/<int:audio_id>/', views.delete_audio, name='delete_audio'),
    path('favorite/<int:audio_id>/', views.toggle_favorite, name='toggle_favorite'),
    path('favorites/', views.list_favorites, name='list_favorites'),
    path('soundboard/', views.soundboard_view, name='soundboard_view'),
    path('soundboard/upload', views.soundboard_upload_view, name='soundboard_upload_view'),
    path('soundboard/<int:pk>/', views.soundboard_view, name='soundboard_view'),
    path('my-soundboards/', views.my_soundboards_view, name='my_soundboards'),
    path('soundboard/delete/<int:pk>/', views.delete_soundboard, name='delete_soundboard'),
    path('register/', views.register_view, name='register'),
    path('my-sounds/', views.my_sounds_view, name='my_sounds'),
    path('password_reset/', ResetPasswordView.as_view(), name='password_reset'),
    path('password_reset_confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='soundbored/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password_reset_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='soundbored/password_reset_complete.html'),
         name='password_reset_complete'),
]

