// index-scripts.js
document.addEventListener("DOMContentLoaded", function () {
  const form = document.querySelector("form");

  form.addEventListener("submit", function (event) {
    let valid = true;
    const inputs = form.querySelectorAll('input[type="number"]');

    inputs.forEach((input) => {
      if (input.value === "") {
        valid = false;
        input.style.borderColor = "#e74c3c"; // Red border
      } else {
        input.style.borderColor = "#ddd";
      }
    });

    if (!valid) {
      event.preventDefault();
      alert("Please fill out all required fields.");
    }
  });
});
