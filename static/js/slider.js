let slideIndex = 0;
showSlides();

function showSlides() {
    let i;
    let slides = document.getElementsByClassName("mySlides");
    for (i = 0; i < slides.length; i++) {
        slides[i].classList.remove("visible");
    }
    slideIndex++;
    if (slideIndex > slides.length) {
        slideIndex = 1;
    }
    slides[slideIndex - 1].classList.add("visible");
    setTimeout(showSlides, 2000);
}

document.getElementById('flecha-izquierda').addEventListener('click', function() {
  changeSlide(-1);
});

document.getElementById('flecha-derecha').addEventListener('click', function() {
  changeSlide(1);
});

function changeSlide(n) {
  let slides = document.getElementsByClassName("mySlides");
  for (let i = 0; i < slides.length; i++) {
    slides[i].classList.remove("visible");
  }
  slideIndex += n;
  if (slideIndex > slides.length) {
    slideIndex = 1;
  }
  if (slideIndex < 1) {
    slideIndex = slides.length;
  }
  slides[slideIndex - 1].classList.add("visible");
}