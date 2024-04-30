from django.shortcuts import render, redirect, get_object_or_404
from .forms import AudioForm
from .models import Audio
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .forms import NewUserForm


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

# Upload view


@login_required
def audio_upload_view(request):
    if request.method == 'POST':
        form = AudioForm(request.POST, request.FILES)
        if form.is_valid():
            audio = form.save(commit=False)
            audio.uploader = request.user  # Set the uploader to the current user
            audio.save()
            return redirect('my_sounds')  # Redirect to 'My Sounds' view after upload
    else:
        form = AudioForm()
    return render(request, 'soundbored/audio_upload.html', {'form': form})

# Favorites


@login_required
def toggle_favorite(request, audio_id):
    audio = get_object_or_404(Audio, pk=audio_id)
    if request.user in audio.favorites.all():
        audio.favorites.remove(request.user)
    else:
        audio.favorites.add(request.user)
    return redirect('audio_list')

# My Sounds View
@login_required
def my_sounds_view(request):
    user_audios = request.user.uploaded_audios.all()  # Fetch audios uploaded by the user
    return render(request, 'soundbored/my_sounds.html', {'audios': user_audios})



# Favorites View


@login_required
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
