document.addEventListener("DOMContentLoaded", function () {
    const dropdownBtn = document.querySelector(".dropbtn");
    const dropdownContent = document.querySelector(".dropdown-content");

    // Toggle dropdown on button click
    dropdownBtn.addEventListener("click", function (event) {
        event.stopPropagation();
        dropdownContent.classList.toggle("show");
    });

    // Close dropdown when clicking outside
    document.addEventListener("click", function () {
        dropdownContent.classList.remove("show");
    });
});
document.addEventListener("DOMContentLoaded", function () {
  const dropdownToggle = document.querySelector(".dropdown-toggle");
  const dropdownMenu = document.querySelector(".dropdown-menu");
  const selectedLanguage = document.querySelector(".selected-language");

  // Language mapping for display
  const langMap = {
      en: "🇬🇧 English",
      es: "🇪🇸 Español",
      ar: "🇸🇦 العربية"
  };

  // Load saved language preference
  const savedLang = localStorage.getItem("selectedLanguage") || "en";
  selectedLanguage.innerHTML = langMap[savedLang];

  // Toggle dropdown menu
  dropdownToggle.addEventListener("click", function () {
      dropdownMenu.style.display = dropdownMenu.style.display === "block" ? "none" : "block";
  });

  // Select language and update UI
  dropdownMenu.addEventListener("click", function (e) {
      if (e.target.tagName === "LI") {
          const lang = e.target.getAttribute("data-lang");
          if (lang) {
              selectedLanguage.innerHTML = langMap[lang]; // Update UI
              localStorage.setItem("selectedLanguage", lang); // Save preference
              dropdownMenu.style.display = "none"; // Hide dropdown
          }
      }
  });

  // Hide dropdown when clicking outside
  document.addEventListener("click", function (e) {
      if (!dropdownToggle.contains(e.target) && !dropdownMenu.contains(e.target)) {
          dropdownMenu.style.display = "none";
      }
  });
});
let list = document.querySelector('.slider .list');
let items = document.querySelectorAll('.slider .list .item');
let dots = document.querySelectorAll('.slider .dits li');
let prev = document.getElementById('prev');
let next = document.getElementById('next');

let active = 0;
let lengthItems = items.length - 1;

next.onclick = function(){
    if (active + 1 > lengthItems){
        active = 0;
    } else {
        active = active + 1;
    }
    reloadSlider();
}
function reloadSlider(){
    let checkLeft = item[active].offsetLeft;
    list.style.left = -checkLeft + 'px';

    let lastActiveDot = document.querySelector('.slider .dots li.active');
    lastActiveDot.classList.remove('active');
    dots[active].classList.add('active');
}