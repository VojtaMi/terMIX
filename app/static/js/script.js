// Function to highlight the active page link
document.addEventListener("DOMContentLoaded", function() {
    var navLinks = document.querySelectorAll('.nav-link');
    var currentUrl = new URL(window.location.href).pathname;

    navLinks.forEach(function(link) {
        if (link.getAttribute('href') && link.getAttribute('href') !== '#') {
            var linkUrl = new URL(link.href).pathname;
            if (linkUrl === currentUrl) {
                link.classList.add('active');
                link.setAttribute('aria-current', 'page');
            }
        }
    });
});


// Function to highlight the active language link
document.addEventListener("DOMContentLoaded", function() {
    var langLinks = document.querySelectorAll('.lang-link');

    // Extract the current language from the URL path (e.g., /cs/ or /en/)
    var currentLang = window.location.pathname.split('/')[1]; // Get the first part of the path

    langLinks.forEach(function(link) {
        var linkLang = link.getAttribute('href').split('/')[1]; // Get the first part of the href path
        if (linkLang === currentLang) {
            link.classList.add('active');
        } else {
            link.classList.remove('active');
        }
    });
});

