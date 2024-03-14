function question(baechu, money) {
  // 여기에서 코드 작성해주세요!
  let result;
  result = money - baechu * 3000;
  return result;
}

const change = document.querySelector("p");

alert("배추 한 개당 가격이 3000원 입니다 구입하시겠습니까?");

let baechu = prompt("배추 몇개 구입하시겠습니까?");
let money = prompt("3000원 이상 지불해 주세요.");

let result = question(baechu, money);

change.textContent = `결제완료되었습니다. 거스름돈은 ${result}원 입니다.`;
