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

// Poster image slideshow
document.addEventListener("DOMContentLoaded", () => {
    const el = document.getElementById("poster");
    if (!el) return;

    const background = el.querySelector(".poster-background") || el;
    const posters = JSON.parse(el.dataset.posters || "[]");

    if (!posters.length) return;

    let index = 0;

    const setBackground = (url) => {
        background.style.backgroundImage = `url('${url}')`;
    };

    // Set initial image
    setBackground(posters[0]);

    const intervalMs = 6000;      // time each image is shown
    const fadeMs = 600;           // must match CSS transition

    if (posters.length === 1) return;

    setInterval(() => {
        index = (index + 1) % posters.length;
        const nextUrl = posters[index];

        // fade out
        background.classList.add("fade-out");

        // after fade-out, switch image and fade back in
        setTimeout(() => {
            setBackground(nextUrl);
            background.classList.remove("fade-out");
        }, fadeMs);
    }, intervalMs);
});
