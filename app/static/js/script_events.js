window.addEventListener('load', function() {
  const flipCard = document.getElementById('flipCard');
  const flipCardImage = document.getElementById('flipCardImage');

  // Ensure the card adjusts to the image size
  flipCardImage.onload = function() {
    const cardWidth = flipCardImage.clientWidth;
    const cardHeight = flipCardImage.clientHeight;

    flipCard.style.width = `${cardWidth}px`;
    flipCard.style.height = `${cardHeight}px`;
  };

  // Handle the case when the image might already be cached and loaded
  if (flipCardImage.complete) {
    flipCardImage.onload(); // Trigger the resize
  }
});
