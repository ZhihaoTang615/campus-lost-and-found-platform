const lostItemForm = document.querySelector("#lost-item-form");
const foundItemForm = document.querySelector("#found-item-form");

if (lostItemForm) {
  lostItemForm.addEventListener("submit", function (event) {
    event.preventDefault();
    alert("Lost item report submitted successfully.");
    lostItemForm.reset();
  });
}

if (foundItemForm) {
  foundItemForm.addEventListener("submit", function (event) {
    event.preventDefault();
    alert("Found item report submitted successfully.");
    foundItemForm.reset();
  });
}
