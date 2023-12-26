const one = document.getElementById("one");
const two = document.getElementById("two");
const three = document.getElementById("three");
const four = document.getElementById("four");
const five = document.getElementById("five");
const six = document.getElementById("six");
const seven = document.getElementById("seven");
const eight = document.getElementById("eight");
const nine = document.getElementById("nine");
const add = document.getElementById("add");
const subtract = document.getElementById("subtract");
const multiply = document.getElementById("multiply");
const divide = document.getElementById("divide");
const equal = document.getElementById("equal");
const clear = document.getElementById("clear");
let num1, num2, operator;

const numlClick = function (e) {
  document.getElementById("input_text").value += e.target.value;
};

const operatorClick = function (e) {
  if (document.getElementById("input_text").value) {
    num1 = document.getElementById("input_text").value;
    document.getElementById("input_text").value = "";
    operator = e.target.value;
  } else {
    alert("숫자를 입력하세요.");
  }
};

const resultClick = function () {
  if (document.getElementById("input_text").value) {
    if (operator) {
      num2 = document.getElementById("input_text").value;
      if (operator === "+") {
        document.getElementById("input_text").value =
          parseInt(num1) + parseInt(num2);
      } else if (operator === "-") {
        document.getElementById("input_text").value =
          parseInt(num1) - parseInt(num2);
      } else if (operator === "*") {
        document.getElementById("input_text").value =
          parseInt(num1) * parseInt(num2);
      } else if (operator === "/") {
        document.getElementById("input_text").value =
          parseInt(num1) / parseInt(num2);
      }
    }
  } else {
    alert("숫자를 입력하세요.");
  }
};

const clearClick = function () {
  document.getElementById("input_text").value = "";
};

one.addEventListener("click", numlClick);
two.addEventListener("click", numlClick);
three.addEventListener("click", numlClick);
four.addEventListener("click", numlClick);
five.addEventListener("click", numlClick);
six.addEventListener("click", numlClick);
seven.addEventListener("click", numlClick);
eight.addEventListener("click", numlClick);
nine.addEventListener("click", numlClick);
zero.addEventListener("click", numlClick);

add.addEventListener("click", operatorClick);
subtract.addEventListener("click", operatorClick);
multiply.addEventListener("click", operatorClick);
divide.addEventListener("click", operatorClick);
clear.addEventListener("click", clearClick);
equal.addEventListener("click", resultClick);
