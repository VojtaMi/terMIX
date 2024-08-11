document.addEventListener("DOMContentLoaded", function () {
    function centerElement(element) {
        var el = document.querySelector(element);
        if (el) {
            var elementOffset = el.getBoundingClientRect().top + window.pageYOffset;
            var elementHeight = el.offsetHeight;
            var viewportHeight = window.innerHeight;

            // Calculate the scroll position to center the element
            var scrollTop = elementOffset - (viewportHeight / 2) + (elementHeight / 2);

            // Smoothly scroll to the calculated position
            window.scrollTo({
                top: scrollTop,
                behavior: 'smooth'
            });
        }
    }

    // Center the carousel when the page loads
    centerElement('#myCarousel');
});
