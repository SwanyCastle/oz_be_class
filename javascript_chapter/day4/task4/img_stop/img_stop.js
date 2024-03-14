const img = document.getElementById("img_moon");
// const start_btn = document.getElementById("start");
const stop_btn = document.getElementById("stop");

let img_arr = [
  "images/moon_cheers.png",
  "images/moon_crying.png",
  "images/moon_dream.png",
  "images/moon_eat.png",
  "images/moon_hungry.png",
];
let currentIndex = 0;
// let img_interval;

function chage_Img() {
  img.src = img_arr[currentIndex];
  currentIndex = (currentIndex + 1) % img_arr.length;
}

// function start() {
//   img_interval = setInterval(chage_Img, 1000);
// }

let img_interval = setInterval(chage_Img, 1000);

function stop() {
  clearInterval(img_interval);
}

// start_btn.addEventListener("click", start);
stop_btn.addEventListener("click", stop);
