document.addEventListener('DOMContentLoaded', function () {
    var clickableImage = document.getElementById('menu_image');
    var targetElement = document.getElementById("target_element");

    var isClicked = false;

    clickableImage.addEventListener('click', function () {
        isClicked = !isClicked;

        if (isClicked) {
            // Change CSS property of the target element
            targetElement.style.display = "block";
        } else {
            targetElement.style.display = "none";
        }
    });
});
