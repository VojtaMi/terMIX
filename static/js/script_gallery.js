$(document).ready(function () {
    function centerElement(element) {
        var $element = $(element);
        if ($element.length) {
            var elementOffset = $element.offset().top;
            var elementHeight = $element.outerHeight();
            var viewportHeight = $(window).height();

            // Calculate the scroll position to center the element
            var scrollTop = elementOffset - (viewportHeight / 2) + (elementHeight / 2);

            // Smoothly scroll to the calculated position
            $('html, body').animate({
                scrollTop: scrollTop
            });
        }
    }

    // Center the carousel when the page loads
    centerElement('#myCarousel');
});