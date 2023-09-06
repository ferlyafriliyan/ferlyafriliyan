// Code JavaScript
const hamburger = document.querySelector('.hamburger');
const links = document.querySelector('.links');
const linksList = document.querySelectorAll('.links li a');

hamburger.addEventListener('click', function() {
  links.classList.toggle('show');
});

linksList.forEach(function(link) {
  link.addEventListener('click', function() {
    links.classList.remove('show');
  });
});
