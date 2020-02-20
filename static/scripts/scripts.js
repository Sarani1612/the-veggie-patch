
// Opens modal when user clicks on the button to edit a recipe
var modal = document.getElementById("edit-modal");
var button = document.getElementById("modal-button");

button.onclick = function() {
  modal.style.display = "block";
}

window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}