document.addEventListener("DOMContentLoaded", function () {
  var submitBtn = document.getElementById("submit");

  var location = document.getElementById("location");
  var female = document.getElementById("female");
  var male = document.getElementById("male");

  submitBtn.addEventListener("click", function () {
    console.log(document.getElementById("email").value);
    console.log(document.getElementById("name").value);
    console.log(document.getElementById("pwd").value);
    console.log(document.getElementById("pwd_chk").value);
    console.log(document.getElementById("tel1").value);
    console.log(document.getElementById("tel2").value);
    console.log(document.getElementById("tel3").value);
    console.log(document.getElementById("location").value);
    console.log(document.getElementById("female").checked);
    console.log(document.getElementById("male").checked);
  });
});
