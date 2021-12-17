const toggleButton = document.getElementsByClassName('burger-meny')[0]
const navbarLinks = document.getElementsByClassName('meny-lenker')[0]

toggleButton.addEventListener('click', () => {
    navbarLinks.classList.toggle('active')
})

function myFunction1() {
    var x = document.getElementById("løsning1");
    if (x.style.display === "none") {
      x.style.display = "block";
    } else {
      x.style.display = "none";
    }
  }

  function myFunction2() {
    var x = document.getElementById("løsning2");
    if (x.style.display === "none") {
      x.style.display = "block";
    } else {
      x.style.display = "none";
    }
  }