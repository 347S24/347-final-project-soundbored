from django.shortcuts import render, redirect
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