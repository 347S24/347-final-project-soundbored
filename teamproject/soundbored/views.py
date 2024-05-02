from django.shortcuts import render, redirect, get_object_or_404
from .forms import AudioForm, SoundBoardForm, NewUserForm
from .models import Audio, SoundBoard
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .forms import NewUserForm
from .forms import EmailForm
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from django import template


# Login Veiw for user authentication
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        # User exists
        if user is not None:
            login(request, user)
            # Redirect to home
            return redirect('audio_list')
        # User doesn't exist
        else:
            error_message = 'Invalid username or password'
            return render(request, 'soundbored/login.html', {'error_message': error_message})
    return render(request, 'soundbored/login.html')


# Logout Veiw
def logout_view(request):
    logout(request)
    return redirect('audio_list')


# Existing audio list view
def audio_list_view(request):
    audios = Audio.objects.all()
    return render(request, 'soundbored/audio_list.html', {'audios': audios, 'logged_in': request.user.is_authenticated})










# My Soundboards
@login_required
def soundboard_upload_view(request):
    if request.method == 'POST':
        form = SoundBoardForm(request.POST)
        if form.is_valid():
            new_soundboard = SoundBoard(
                title=form.cleaned_data['title'],
                owner=request.user
            )
            new_soundboard.save()
            new_soundboard.audios.set(form.cleaned_data['audios'])
            new_soundboard.save()
            # Redirect to the 'My Soundboards' view after successful upload
            return redirect('my_soundboards')
    else:
        form = SoundBoardForm()
    audios = Audio.objects.all()
    return render(request, 'soundbored/soundboard_upload.html', {'form': form, 'audios': audios})


@login_required
def my_soundboards_view(request):
    soundboards = SoundBoard.objects.filter(owner=request.user)
    return render(request, 'soundbored/my_soundboards.html', {'soundboards': soundboards})


@login_required
def soundboard_view(request, pk=None):
    if pk:
        soundboard = get_object_or_404(SoundBoard, pk=pk)
    else:
        return redirect('my_soundboards')

    return render(request, 'soundbored/soundboard.html', {'soundboard': soundboard})

# used for refffffffrence 
# @login_required
# def soundboard_detail_view(request, pk):
#     soundboard = get_object_or_404(SoundBoard, pk=pk, owner=request.user)  # Ensure ownership
#     if request.method == 'POST':
#         form = SoundBoardForm(request.POST, instance=soundboard)
#         if form.is_valid():
#             form.save()
#             return redirect('soundboard_detail', pk=soundboard.pk)
#     else:
#         form = SoundBoardForm(instance=soundboard)
#     return render(request, 'soundbored/soundboard_detail.html', {'form': form, 'soundboard': soundboard})


@login_required
def delete_soundboard(request, pk):
    soundboard = get_object_or_404(SoundBoard, pk=pk, owner=request.user)  # Ensures that only the owner can delete
    soundboard.delete()
    return redirect('my_soundboards')  # Redirects back to the list of soundboards











# Upload view
@ login_required
def audio_upload_view(request):
    if request.method == 'POST':
        form = AudioForm(request.POST, request.FILES)
        if form.is_valid():
            audio = form.save(commit=False)
            audio.uploader = request.user  # Set the uploader to the current user
            audio.save()
            # Redirect to 'My Sounds' view after upload
            return redirect('my_sounds')
    else:
        form = AudioForm()
    return render(request, 'soundbored/audio_upload.html', {'form': form})


# Favorites
@ login_required
def toggle_favorite(request, audio_id):
    audio = get_object_or_404(Audio, pk=audio_id)
    if request.user in audio.favorites.all():
        audio.favorites.remove(request.user)
    else:
        audio.favorites.add(request.user)
    # Return to current url after toggled
    return redirect(request.META.get('HTTP_REFERER'))


# My Sounds View
@ login_required
def my_sounds_view(request):
    # Fetch audios uploaded by the user
    user_audios = request.user.uploaded_audios.all()
    return render(request, 'soundbored/my_sounds.html', {'audios': user_audios, 'delete_button': True})


# Favorites View
@ login_required
def list_favorites(request):
    user_favorites = request.user.favorite_audios.all()
    return render(request, 'soundbored/favorites_list.html', {'favorites': user_favorites})


def delete_audio(request, audio_id):
    # Get the audio object, and if it doesn't exist, return a 404 error
    audio = get_object_or_404(Audio, pk=audio_id)
    audio.delete()  # Delete the audio object
    return redirect('my_sounds')  # Redirect to the audio list page


def add_favorite(request, audio_id):
    # Get the audio object, and if it doesn't exist, return a 404 error
    audio = get_object_or_404(Audio, pk=audio_id)
    audio.is_favorite = not audio.is_favorite  # Toggle the favorite status
    audio.save()
    return redirect('audio_list')  # Redirect to the audio list page


def register_view(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            # If you want to log the user in and redirect to a new page:
            # login(request, user)
            # redirect to the desired page
            return redirect(reverse('login'))  # Redirect them to login page
    else:
        form = NewUserForm()
    return render(request, 'soundbored/register.html', {"form": form})


def password_reset(request):
    form = EmailForm()
    return render(request, 'soundbored/password_reset_form.html', {'form': form})


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'soundbored/password_reset.html'
    email_template_name = 'soundbored/password_reset_email.html'
    subject_template_name = 'soundbored/password_reset_subject.txt'
    success_message = "We've emailed you instructions for setting your password, " \
        "if an account exists with the email you entered. You should receive them shortly." \
        " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('password_reset')
