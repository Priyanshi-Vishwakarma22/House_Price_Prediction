const form = document.querySelector("form");
const button = document.querySelector("button");

form.addEventListener("submit", function (e) {

    // Get Values
    const bedrooms = Number(document.getElementById("bedrooms").value);
    const bathrooms = Number(document.getElementById("bathrooms").value);
    const stories = Number(document.getElementById("stories").value);
    const parking = Number(document.getElementById("parking").value);

    // Bedrooms Validation
    if (bedrooms < 1 || bedrooms > 6) {
        alert("Bedrooms must be between 1 and 6.");
        document.getElementById("bedrooms").focus();
        e.preventDefault();
        return;
    }

    // Bathrooms Validation
    if (bathrooms < 1 || bathrooms > 4) {
        alert("Bathrooms must be between 1 and 4.");
        document.getElementById("bathrooms").focus();
        e.preventDefault();
        return;
    }

    // Stories Validation
    if (stories < 1 || stories > 4) {
        alert("Stories must be between 1 and 4.");
        document.getElementById("stories").focus();
        e.preventDefault();
        return;
    }

    // Parking Validation
    if (parking < 0 || parking > 3) {
        alert("Parking must be between 0 and 3.");
        document.getElementById("parking").focus();
        e.preventDefault();
        return;
    }

    // Loading Button
    button.innerHTML =
        '<i class="fa-solid fa-spinner fa-spin"></i> Predicting...';

    button.disabled = true;

});