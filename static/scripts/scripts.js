window.onload = function(){

    // Opens modal when user clicks on the button to edit a recipe
    var modal = document.getElementById("edit-modal");
    var button = document.getElementById("modal-button");

    button.onclick = function () {
        modal.style.display = "block";
    };

    // Closes modal when clicking outside of it
    window.onclick = function (event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    };

    // Ensures modal is kept open if the wrong key was entered to avoid having to click the button again
    if ($('#wrong_key').length)
        modal.style.display = "block";

    // Removes flash messages after 5 seconds
    setTimeout(function () {
        $('.alert').remove();}, 5000
        )

    };