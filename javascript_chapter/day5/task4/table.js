const table = document.getElementById("table");
const result = document.getElementById("result");

// let name_arr = ["짱구", "맹구", "철수", "훈이", "유리", "수지"];
// let score_arr = [45, 75, 95, 50, 68, 86];

let name_score = {
  짱구: 45,
  맹구: 75,
  철수: 95,
  훈이: 50,
  유리: 68,
  수지: 86,
};

window.addEventListener("load", function () {
  let name_select = [];

  for (let key in name_score) {
    const newRow = table.insertRow();

    const newCell_name = newRow.insertCell(0);
    const newCell_score = newRow.insertCell(1);

    newCell_name.innerText = key;
    newCell_score.innerText = name_score[key];

    if (name_score[key] >= 75) {
      name_select.push(key);
    }
  }

  let sort_name = name_select.sort();
  let result_name = sort_name.reverse();

  result.textContent = `75점이 넘는 사람 : ${result_name.join(", ")}`;
});
