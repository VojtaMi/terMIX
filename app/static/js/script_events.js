document.addEventListener('DOMContentLoaded', function () {
        var flipCards = document.querySelectorAll('.flip-card');

        flipCards.forEach(function (card) {
            card.addEventListener('click', function () {
                this.querySelector('.flip-card-inner').classList.toggle('is-flipped');
            });
        });
    });