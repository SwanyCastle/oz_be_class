const todaySpan = document.getElementById("today");
const numberDiv = document.querySelector(".numbers");
const drawButton = document.getElementById("draw");
const resetButton = document.getElementById("reset");

const today = new Date();

let year = today.getFullYear();
let month = today.getMonth() + 1;
let date = today.getDate();
todaySpan.textContent = `${year}년 ${month}월 ${date}일 `;

let lottoNumbers = [];
let isClicked = false;

function paintNumber(randNum) {
  const eachNumDiv = document.createElement("div");
  eachNumDiv.classList.add("eachnum");
  eachNumDiv.textContent = randNum;
  numberDiv.append(eachNumDiv);
}

drawButton.addEventListener("click", function () {
  if (!isClicked) {
    isClicked = true;
    while (lottoNumbers.length < 6) {
      let rn = Math.floor(Math.random() * 45) + 1;
      if (lottoNumbers.indexOf(rn) === -1) {
        lottoNumbers.push(rn);
        paintNumber(rn);
      }
    }
  } else {
    lottoNumbers.splice(0, lottoNumbers.length);
    numberDiv.innerHTML = "";
    isClicked = false;
  }
});

resetButton.addEventListener("click", function () {
  lottoNumbers.splice(0, lottoNumbers.length);
  numberDiv.innerHTML = "";
});
