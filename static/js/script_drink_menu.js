// Function to display the list of ingredients for a cocktail
document.addEventListener('DOMContentLoaded', function () {
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
});

// Function to style drink button when clicked
document.querySelectorAll('.button-header').forEach(function(button) {
    button.addEventListener('click', function() {
        this.classList.toggle('clicked');
    });
});