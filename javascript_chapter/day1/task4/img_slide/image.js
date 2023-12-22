document.addEventListener("DOMContentLoaded", function () {
  var clickedBtnblack = document.getElementById("black");
  var screenElement = document.getElementById("screen");

  var clickedBtn1 = document.getElementById("1");
  var clickedBtn2 = document.getElementById("2");
  var clickedBtn3 = document.getElementById("3");
  var clickedBtnNext = document.getElementById("next");
  var imgElement = document.getElementById("back_img");

  var images = [
    "images/moon.png",
    "images/moon_fighting.png",
    "images/moon_tired.png",
  ];

  var isClicked = false;
  var currentImageIndex = 0;

  clickedBtnblack.addEventListener("click", function () {
    isClicked = !isClicked;

    if (isClicked) {
      // Change CSS property of the target element
      screenElement.style.backgroundColor = "black";
    } else {
      screenElement.style.backgroundColor = "white";
    }
  });

  clickedBtn1.addEventListener("click", function () {
    imgElement.src = "images/moon.png";
  });
  clickedBtn2.addEventListener("click", function () {
    imgElement.src = "images/moon_fighting.png";
  });
  clickedBtn3.addEventListener("click", function () {
    imgElement.src = "images/moon_tired.png";
  });

  clickedBtnNext.addEventListener("click", function () {
    currentImageIndex = (currentImageIndex + 1) % images.length;
    // 새로운 이미지로 변경
    imgElement.src = images[currentImageIndex];
    console.log(currentImageIndex);
  });
});
