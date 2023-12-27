const coment = document.getElementById("coment");
const com = document.getElementById("com");
const me = document.getElementById("me");
const rock = document.getElementById("rock");
const scissors = document.getElementById("scissors");
const paper = document.getElementById("paper");

function rand_com() {
  let randomNumber = Math.floor(Math.random() * 3) + 1;
  return randomNumber;
}

rock.addEventListener("click", function () {
  let randNum = rand_com();
  if (randNum === 1) {
    coment.style.color = "black";
    coment.textContent = "비겼습니다.";
    com.textContent = "상대 : ✊";
    me.textContent = "나 : ✊";
  } else if (randNum === 2) {
    coment.style.color = "blue";
    coment.textContent = "이겼습니다.";
    com.textContent = "상대 : 👆";
    me.textContent = "나 : ✊";
  } else if (randNum === 3) {
    coment.style.color = "red";
    coment.textContent = "졌습니다.";
    com.textContent = "상대 : ✋";
    me.textContent = "나 : ✊";
  }
});

scissors.addEventListener("click", function () {
  let randNum = rand_com();
  if (randNum === 1) {
    coment.style.color = "red";
    coment.textContent = "졌습니다.";
    com.textContent = "상대 : ✊";
    me.textContent = "나 : 👆";
  } else if (randNum === 2) {
    coment.style.color = "black";
    coment.textContent = "비겼습니다.";
    com.textContent = "상대 : 👆";
    me.textContent = "나 : 👆";
  } else if (randNum === 3) {
    coment.style.color = "blue";
    coment.textContent = "이겼습니다.";
    com.textContent = "상대 : ✋";
    me.textContent = "나 : 👆";
  }
});

paper.addEventListener("click", function () {
  let randNum = rand_com();
  if (randNum === 1) {
    coment.style.color = "blue";
    coment.textContent = "이겼습니다.";
    com.textContent = "상대 : ✊";
    me.textContent = "나 : ✋";
  } else if (randNum === 2) {
    coment.style.color = "red";
    coment.textContent = "졌습니다.";
    com.textContent = "상대 : 👆";
    me.textContent = "나 : ✋";
  } else if (randNum === 3) {
    coment.style.color = "black";
    coment.textContent = "비겼습니다.";
    com.textContent = "상대 : ✋";
    me.textContent = "나 : ✋";
  }
});
