var currentTime = new Date();
document.getElementById("today").innerHTML = "현재 시간 : " + currentTime;

var endOfYear = new Date(new Date().getFullYear(), 11, 31, 23, 59, 59);

function diffTime() {
  var timeDiff = endOfYear - currentTime;

  var days = Math.floor(timeDiff / (1000 * 60 * 60 * 24));
  var hours = Math.floor((timeDiff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  var minutes = Math.floor((timeDiff % (1000 * 60 * 60)) / (1000 * 60));
  var seconds = Math.floor((timeDiff % (1000 * 60)) / 1000);

  document.getElementById("remainTime").innerHTML =
    "올해의 남은 시간 : " +
    days +
    "일 " +
    hours +
    "시 " +
    minutes +
    "분 " +
    seconds +
    "초";
}

diffTime();
setInterval(diffTime, 1000);
