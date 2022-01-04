const toggleButton = document.getElementsByClassName('burger-meny')[0]
const navbarLinks = document.getElementsByClassName('meny-lenker')[0]

toggleButton.addEventListener('click', () => {
    navbarLinks.classList.toggle('active')
})


  function myFunction(divid) {
    var x = document.getElementById(divid);
    if (x.style.display === "none") {
      x.style.display = "block";
    } else {
      x.style.display = "none";
    }
  }

  // Slå av "bryteren"
  myFunction(`løsning1`);
  myFunction(`løsning2`);
  myFunction(`løsning3`);

  