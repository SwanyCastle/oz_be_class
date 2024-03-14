var h3 = document.querySelector("h3");
var h4 = document.querySelector("h4");
var h5 = document.querySelector("h5");

const random = Math.floor(Math.random() * 100 + 1);
// h4.textContent = random;

function check_click() {
  let input_num = parseInt(document.getElementById("user_input").value);
  if (input_num < 0) {
    h3.textContent = "0이 아닌 양의 정수를 입력하세요.";
  } else {
    if (input_num > 100) {
      h3.textContent = "100이하의 양의 정수를 입력하세요.";
    } else {
      if (input_num === random) {
        h3.textContent = "정답입니다.";
        alert("정답입니다.");
      } else if (input_num > random) {
        h3.textContent = `${input_num} 보다 작아요`;
      } else if (input_num < random) {
        h3.textContent = `${input_num} 보다 커요`;
      }
    }
  }
}
