document.addEventListener('DOMContentLoaded', function() {
    
    ////////// Navigation mobile nav logic //////////

    const navigation = document.querySelector('.navigation');
    const navigationToggle = document.querySelector('.navigation__toggle');
    const navigationToggleBtn = document.querySelector('.navigation__toggle-btn');
    const navigationLinks = document.querySelector('.navigation__links');
    const navigationModalOverlay = document.querySelector('.navigation__modal-overlay');

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


    ////////// Job like/unlike logic //////////

    const likeButton = document.querySelector('job__button-like');

    // Add click event listener to the like button
    likeButton.addEventListener('click', function () {
        likeButton.classList.remove('.fa-regular fa-bookmark');
        likeButton.classList.add('.fa-solid fa-bookmark')
    })

    ////////// Job filter form logic //////////

    const categorySearchInput = document.querySelector('#category-search');
    const categorySearchOptions = document.querySelectorAll('#search-options option');
    const autocompleteOptions = Array.from(categorySearchOptions).map(option => option.value);

    // Add click event listener to search form inputs
    categorySearchInput.addEventListener('input', () => {
      // Select form input value
      const inputValue = categorySearchInput.value;
      // If input has a value
      if (inputValue.length > 0) {
        // Select items that start with value in input
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


    ////////// Job filter mobile logic //////////

    const filterIcon = document.querySelector('#job__filtering-mobile-btn');
    const jobFilterModal = document.querySelector('#job__filter-modal');
    const jobFiltersMobile = document.querySelectorAll('#job_filter-mobile')

    // Add click event listener to the mobile filter icon
    filterIcon.addEventListener('click', function () {
      // Toggle 'open' class
      jobFilterModal.classList.toggle('open');
      // Toggle 'open' class on modal with filter options
      jobFiltersMobile.classList.toggle('open');
    })
});
  