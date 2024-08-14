
document.getElementById('display-map-button').addEventListener('click', function() {
    // Hide the map-button-container
    document.getElementById('map-button-container').classList.add('d-none');

    // Show the iframe-container
    document.getElementById('map-iframe-container').classList.remove('d-none');
});
