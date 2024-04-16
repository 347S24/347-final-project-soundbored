from django.shortcuts import render, redirect, get_object_or_404
from .forms import AudioForm
from .models import Audio

# Existing audio list view
def audio_list_view(request):
    audios = Audio.objects.all()
    return render(request, 'soundbored/audio_list.html', {'audios': audios})

# Add this new upload view
def audio_upload_view(request):
    if request.method == 'POST':
        form = AudioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('audio_list')  # Redirect to the audio list view after successful upload
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