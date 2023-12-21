/*   문제 출제
 *
 *   🍬 사탕 나누기
 * - A가 가지고 있는 candies를 N명의 friends에게 공평하게 나누어 줄 때,
 * - 각 friends가 가져갈 수 있는 candies의 개수를 구하는 함수를 작성하세요.
 *
 * ❗️ 제한 조건 ❗️
 * - 입력되는 수는 양의 정수입니다.
 * - 반환되는 값은 정수로 나와야 합니다.
 *
 */

function question(candies, friends) {
  // 여기에서 코드 작성해주세요!
  let result;
  result = parseInt(candies / friends);
  return result;
}

let candies = prompt("A가 가지고 있는 사탕은 몇개 입니까?");
let friends = prompt("친구는 총 몇명 입니까?");

const share = document.querySelector("p");

let result = question(candies, friends);

share.textContent = `총 ${friends}명에게 사탕을 ${result}개 씩 나누어 주었습니다. 
남은 사탕 : ${candies - result * friends}개`;
