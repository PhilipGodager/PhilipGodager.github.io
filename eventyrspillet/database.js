// Your web app's Firebase configuration
const firebaseConfig = {
    //Legg inn informasjon for din Firestore Firebase her
    apiKey: "AIzaSyAx03iwtIvMOu_cp2iwPOlvWVi2KxZ8Rgk",
    authDomain: "database-8f5d9.firebaseapp.com",
    projectId: "database-8f5d9",
    storageBucket: "database-8f5d9.appspot.com",
    messagingSenderId: "92624426733",
    appId: "1:92624426733:web:4d1b2a0f899505789bdee4"
};

// Initialize Firebase
firebase.initializeApp(firebaseConfig);

// Lager en referanse til databasen
let db = firebase.firestore();

// Elementer fra DOM
let hovedEl = document.querySelector("#hoved")
let fornavnEl = document.querySelector("#fornavn")
let etternavnEl = document.querySelector("#etternavn")
let registrerBtn = document.querySelector("#registrer")

//Legger til lytter
registrerBtn.addEventListener("click", addUser)

let collectionName = "brukere"


//Funksjon som legger til ny bruker i databasen
function addUser() {
    if(fornavnEl.value != "" && etternavnEl.value != ""){
        /*console.log(fornavnEl.value)
    console.log(etternavnEl.value)
    console.log(alderEl.value)*/
    db.collection(collectionName).add({
        fornavn: fornavnEl.value,
        etternavn: etternavnEl.value,
    })


    //Tømmer input felt
    fornavnEl.value = ""
    etternavnEl.value = ""

    console.log("Brukeren er lagt inn i databasen")
    //Henter brukerne på nytt
    getUsers()
    }

    else(
        alert("Du må skrive inn navnet ditt")
    )   
}

//Man kan eksempelvis skrive .orderBy("fornavn") etter (collectionName) for å sortere etter "fornavn"
function getUsers() {
    // Henter data. Når dataene er ferdig hentet, starter "then"-biten
    db.collection(collectionName).get().then((snapshot) => {
        // Henter ut dokumentene
        let dokumenter = snapshot.docs;

        hovedEl.innerHTML = `<h1 style="font-size: 40px; color: white;">De siste 10 spillerne som har klart å vinne</h1>` // Dette er usortert, ellers måtte man lagt inn klokkeslett for å logge de som var først osv.
        

        // Går gjennom dokumentene
        for (let i = 0; i < 10; i++) { //i < 10 slik at man kun får med de 10 siste
            // Henter data for en enkelt bruker
            let bruker = dokumenter[i].data()

            hovedEl.innerHTML += `<h2 class="font-size: 25px; nybruker_tekst" style="font-weight: bold; margin-top: 9px; text-align: center;"> ${i + 1 + "."} spiller</h2>`

            //console.log(bruker)

            hovedEl.innerHTML += `<p style="font-size: 25px; margin-left: 20px; text-align: center;">Fornavn: ${bruker.fornavn}</p>`

            hovedEl.innerHTML += `<p style="font-size: 25px; margin-left: 20px; text-align: center;">Etternavn: ${bruker.etternavn}</p>`

        }
    });

    nybruker.remove(); //Får vekk registreringsfeltet for å unngå forvirring og dobbelregistrering

    document.querySelector("#registrer_deg").style.display = 'none' //Fjerner overskriften "Registrer deg" etter man har registrert seg
    document.querySelector("#localStorage").style.display = 'none'

}

//Local storage til hvor mange ganger man har vært på nettsiden


// Henter element fra DOM
let localStorageEl = document.querySelector("#localStorage");

// Undersøker om localStorage-variabelen er satt
if (localStorage.antallBesok) {
  // Vi gjør om tekst til tall
  localStorage.antallBesok = Number(localStorage.antallBesok) + 1;
} else {
  localStorage.antallBesok = 1;
}

// Oppdaterer teksten i <h1>-elementet
localStorageEl.innerHTML = "Dette er den " + localStorage.antallBesok + ". gangen du vant dette spillet!";


