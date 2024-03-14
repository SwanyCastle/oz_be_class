const result = document.getElementById("result");
const grade_img = document.getElementById("grade_table");

while (true) {
  const score = parseInt(prompt("중간고사 점수를 입력하세요."));
  if (score > 0) {
    if (score >= 90) {
      result.textContent = `나의 중간고사 점수는 ${score}점, 학점은 A !!!`;
    } else if (score >= 80 && score < 90) {
      result.textContent = `나의 중간고사 점수는 ${score}점, 학점은 B !!!`;
    } else if (score >= 70 && score < 80) {
      result.textContent = `나의 중간고사 점수는 ${score}점, 학점은 C !!!`;
    } else if (score >= 60 && score < 70) {
      result.textContent = `나의 중간고사 점수는 ${score}점, 학점은 D !!!`;
    } else {
      result.textContent = `나의 중간고사 점수는 ${score}점, 학점은 F !!!`;
    }
    grade_img.style.display = "block";
    break;
  } else {
    alert("0~100사이의 숫자를 입력하세요. ");
  }
}
