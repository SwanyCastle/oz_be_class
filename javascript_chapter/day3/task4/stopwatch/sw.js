const startBtn = document.getElementById("start");
const stopBtn = document.getElementById("stop");

var startTime;
var isRun = false;

function formatTime(value) {
  if (value < 10) {
    return "0" + value;
  } else {
    return value;
  }
}

function formatMilliseconds(value) {
  if (value < 10) {
    return "00" + value;
  } else if (value < 100) {
    return "0" + value;
  } else {
    return value;
  }
}

function startStopwatch() {
  if (!isRun) {
    isRun = true;
    startTime = new Date().getTime();
    updateStopwatch();
  }
}

function stopStopwatch() {
  isRun = false;
}

function updateStopwatch() {
  if (isRun) {
    var currentTime = new Date().getTime();
    var elapsedTime = currentTime - startTime;

    var minutes = Math.floor(elapsedTime / (1000 * 60));
    var seconds = Math.floor((elapsedTime % (1000 * 60)) / 1000);
    var milliseconds = Math.floor(elapsedTime % 1000);

    document.getElementById("sw").innerHTML =
      formatTime(minutes) +
      ":" +
      formatTime(seconds) +
      ":" +
      formatMilliseconds(milliseconds);

    setTimeout(updateStopwatch, 10);
  }
}

startBtn.addEventListener("click", startStopwatch);
stopBtn.addEventListener("click", stopStopwatch);
