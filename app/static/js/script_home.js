// Home Links at home page scroll to top instead of reloading
document.addEventListener('DOMContentLoaded', function() {
        // Get all home button elements
        var homeButtons = document.querySelectorAll('.home-scroll-up');

        // Define the scroll-to-top function
        function scrollToTop(event) {
            event.preventDefault(); // Prevent the default link behavior
            window.scrollTo({ top: 0, behavior: 'smooth' }); // Scroll to the top
        }

        // Add event listeners to the home buttons
        homeButtons.forEach(function(button) {
            button.addEventListener('click', scrollToTop);
        });
    });

// set uld for title picture
document.addEventListener('DOMContentLoaded', function() {
    var poster = document.getElementById('poster');
    var imageUrl = poster.getAttribute('data-poster-url');
    poster.style.backgroundImage = 'url(' + imageUrl + ')';
});

// Poster image slideshow
document.addEventListener("DOMContentLoaded", () => {
    const el = document.getElementById("poster");
    const posters = JSON.parse(el.dataset.posters || "[]");

    if (!posters.length) return;

    let index = 0;

    // Set initial image
    el.style.backgroundImage = `url('${posters[0]}')`;

    const intervalMs = 6000;      // time each image is shown
    const fadeMs = 600;           // must match CSS transition

    setInterval(() => {
        // next index
        index = (index + 1) % posters.length;
        const nextUrl = posters[index];

        // fade out
        el.classList.add("fade-out");

        // after fade-out, switch image and fade back in
        setTimeout(() => {
            el.style.backgroundImage = `url('${nextUrl}')`;
            el.classList.remove("fade-out");
        }, fadeMs);
    }, intervalMs);
});