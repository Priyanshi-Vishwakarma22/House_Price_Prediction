const form = document.querySelector("form");
const button = document.querySelector("button");

form.addEventListener("submit", function () {

    button.innerHTML =
        '<i class="fa-solid fa-spinner fa-spin"></i> Predicting...';

    button.disabled = true;

});