// Toggle Audio
function togglePlay(audioId) {
  var audio = document.getElementById(audioId);
  if (audio) {
      if (audio.paused) {
          audio.play();
      } else {
          audio.pause();
          audio.currentTime = 0;
      }
  }
}