from django.shortcuts import render, redirect, get_object_or_404
from .forms import AudioForm
from .models import Audio
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


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

def soundboard_view(request):
    audios = Audio.objects.all()
    return render(request, 'soundbored/soundboard.html', {'audios': audios, 'logged_in': request.user.is_authenticated})

# Upload veiw
@login_required
def audio_upload_view(request):
    if request.method == 'POST':
        form = AudioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Redirect to the audio list view after successful upload
            return redirect('audio_list')
    else:
        form = AudioForm()
    return render(request, 'soundbored/audio_upload.html', {'form': form})


def delete_audio(request, audio_id):
    # Get the audio object, and if it doesn't exist, return a 404 error
    audio = get_object_or_404(Audio, pk=audio_id)
    audio.delete()  # Delete the audio object
    return redirect('audio_list')  # Redirect to the audio list page


def add_favorite(request, audio_id):
    # Get the audio object, and if it doesn't exist, return a 404 error
    audio = get_object_or_404(Audio, pk=audio_id)
    audio.is_favorite = not audio.is_favorite  # Toggle the favorite status
    audio.save()
    return redirect('audio_list')  # Redirect to the audio list page
