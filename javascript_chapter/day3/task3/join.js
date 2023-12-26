// 제출 이벤트를 받는다 (이벤트 핼들링)
// 제출된 입력 값들을 참조
// 입력값에 문제가 있는 경우 이를 감지

const form = document.getElementById("form");

form.addEventListener("submit", function (event) {
  event.preventDefault(); // 기존 새로고침 되는 기능 차단

  let usrId = event.target.id.value;
  let usrPw1 = event.target.pw1.value;
  let usrPw2 = event.target.pw2.value;
  let usrName = event.target.name.value;
  let usrPhnum = event.target.phnum.value;
  let usrPosition = event.target.position.value;
  let usrGender = event.target.gender.value;
  let usrEmail = event.target.email.value;
  let usrIntro = event.target.intro.value;

  if (usrId.length < 6) {
    alert("아이디가 너무 짧습니다. 6자 이상 입력해주세요.");
    return;
  }

  if (usrPw1 !== usrPw2) {
    alert("비밀번호가 일치하지 않습니다.");
    return;
  }

  document.body.innerHTML = "";
  document.write(`<h1>${usrId}님 환영합니다.</h1>`);
  document.write(`<h2>회원 가입 시 입력하신 내역은 다음과 같습니다.</h2>`);
  document.write(`<p>아이디 : ${usrId}</p>`);
  document.write(`<p>이름 : ${usrName}</p>`);
  document.write(`<p>전화번호 : ${usrPhnum}</p>`);
  document.write(`<p>원하는 직무 : ${usrPosition}</p>`);

  console.log(
    usrId,
    usrPw1,
    usrPw2,
    usrName,
    usrPhnum,
    usrPosition,
    usrGender,
    usrEmail,
    usrIntro
  );
});
