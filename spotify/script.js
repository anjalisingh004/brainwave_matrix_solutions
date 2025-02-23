// Play and Pause Button Logic
const playPauseButton = document.getElementById('play-pause');
const progressBar = document.getElementById('progress-bar');

let isPlaying = false;

playPauseButton.addEventListener('click', () => {
  isPlaying = !isPlaying;
  playPauseButton.textContent = isPlaying ? 'Pause' : 'Play';

  // Simulate Progress Bar Movement
  if (isPlaying) {
    simulateProgress();
  }
});

function simulateProgress() {
  let progress = parseInt(progressBar.value);
  const interval = setInterval(() => {
    if (!isPlaying || progress >= 100) {
      clearInterval(interval);
    } else {
      progress += 1;
      progressBar.value = progress;
    }
  }, 500);
}
