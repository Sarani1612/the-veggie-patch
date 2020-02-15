
// Opens modal when user clicks on the button to edit a recipe
var modal = document.getElementById("edit-modal");
var btn = document.getElementById("modal-button");

btn.onclick = function() {
  modal.style.display = "block";
}

window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}