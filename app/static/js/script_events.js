document.addEventListener('DOMContentLoaded', function () {
        // Select all flip cards
        var flipCards = document.querySelectorAll('.flip-card');

        // Add event listeners for each flip card
        flipCards.forEach(function (card) {
            // Click event to toggle the flip
            card.addEventListener('click', function () {
                this.querySelector('.flip-card-inner').classList.toggle('is-flipped');
            });

            // Keypress event to toggle the flip
            card.addEventListener('keypress', function (event) {
                // Check if the Enter key (key code 13) or Space key (key code 32) was pressed
                if (event.key === 'Enter' || event.key === ' ') {
                    event.preventDefault(); // Prevent default action (scrolling for Space)
                    this.querySelector('.flip-card-inner').classList.toggle('is-flipped');
                }
            });
        });
    });