// Popup functionality
const videoCards = document.querySelectorAll('.video-card');
const popupOverlay = document.querySelector('.popup-overlay');
const popupIframe = document.querySelector('.popup-content iframe');
const closePopupBtn = document.querySelector('.close-popup');

videoCards.forEach(card => {
    card.addEventListener('click', () => {
        const videoSrc = card.getAttribute('data-video');
        popupIframe.src = videoSrc;
        popupOverlay.classList.add('active');
    });
});

closePopupBtn.addEventListener('click', () => {
    popupOverlay.classList.remove('active');
    popupIframe.src = ''; // Stop the video
});

popupOverlay.addEventListener('click', (e) => {
    if (e.target === popupOverlay) {
        popupOverlay.classList.remove('active');
        popupIframe.src = ''; // Stop the video
    }
});
