let mosterHP = 100;
const container = document.getElementById("container");
const h1 = document.createElement("h1");
h1.textContent = "몬스터 잡기 게임을 시작합니다.";
container.appendChild(h1);

let atttackDamage = parseInt(
  prompt("1회 공격시 데미지는? (양의 정수로 입력하세요)")
);
let atttackCount = 0;

if (atttackDamage > 0) {
  while (mosterHP > 0) {
    mosterHP -= atttackDamage;
    atttackCount++;

    if (mosterHP < 0 || atttackDamage > 100) {
      mosterHP = 0;
    }

    const p = document.createElement("p");
    p.textContent = `몬스터를 ${atttackCount}회 공격했다.`;
    container.append(p);

    const strong = document.createElement("strong");
    strong.textContent = `몬스터의 남은 HP는 ${mosterHP}입니다.`;
    container.append(strong);
  }

  const h2 = document.createElement("h2");
  h2.textContent = "몬스터 잡기 완료.";
  h2.style.color = "orange";
  h2.title = "게임을 다시 시작하고 싶으면 새로고침을 하세요";
  container.append(h2);
} else {
  alert("데미지를 잘못 입력하여 게임을 취소합니다.");
}
