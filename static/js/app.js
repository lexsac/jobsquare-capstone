document.addEventListener('DOMContentLoaded', function() {
    // Get the elements
    const navigation = document.querySelector('.navigation');
    const navigationToggle = document.querySelector('.navigation__toggle');
    const navigationToggleBtn = document.querySelector('.navigation__toggle-btn');
    const navigationLinks = document.querySelector('.navigation__links');
    const navigationModalOverlay = document.querySelector('.navigation__modal-overlay');

    const likeButton = document.querySelector('job__button-like');

    // Add click event listener to the like button
    likeButton.addEventListener('click', function () {
        likeButton.classList.remove('.fa-regular fa-bookmark');
        likeButton.classList.add('.fa-solid fa-bookmark')
    })

    // Add click event listener to the toggle button
    navigationToggle.addEventListener('click', function () {
        // Toggle the "open" class on the navigation
        navigation.classList.toggle('open');
        // Toggle the "open" class on background dark overlay
        navigationModalOverlay.classList.toggle('open');
        // Toggle the "open" class on the hamburger button
        navigationToggle.classList.toggle('open');
        // Toggle the "opend" class on the hamburger button
        navigationToggleBtn.classList.toggle('open');
        // Toggle the "open" class on the navigation links
        navigationLinks.classList.toggle('open');
    });
});
  

const categorySearchInput = document.querySelector('#category-search');
const categorySearchOptions = document.querySelectorAll('#search-options option');
const autocompleteOptions = Array.from(categorySearchOptions).map(option => option.value);

categorySearchInput.addEventListener('input', () => {
  const inputValue = categorySearchInput.value;
  if (inputValue.length > 0) {
    const filteredOptions = autocompleteOptions.filter(option => option.startsWith(inputValue));
    searchOptions.innerHTML = '';
    filteredOptions.forEach(option => {
      const optionElement = document.createElement('option');
      optionElement.value = option;
      searchOptions.appendChild(optionElement);
    });
  } else {
    searchOptions.innerHTML = '';
  }
});


  
  
  