let knappLyd = new Audio('./Lyder/onclick.wav'); //Henter lyd for knapper
knappLyd.volume = 0.3; //Setter volumet til 0.3

let restartLyd = new Audio('./Lyder/restart.wav'); //Henter lyd for restart
restartLyd.volume = 0.3;

let backgroundmusic = new Audio('./Lyder/backgroundmusic.mp3'); // Henter lyd for bakgrunnsmusikk
backgroundmusic.volume = 0.2;

let winLyd = new Audio('./Lyder/win.mp3'); //Henter lyd for når man har vunnet
winLyd.volume = 0.3;

//Henter elementene tekst og valg-knapper
const textElement = document.getElementById('tekst')
const valgKnapperElement = document.getElementById('valg-knapper')

let start = {}

//Viser hva som skjer ved starten, altså her skal teskten med id=1 vises
function startSpill() {
  start = {}
  visTextNode(1)
}

//Funksjonen viser teksten for knappene
function visTextNode(textNodeIndex) {
  const textNode = textNodes.find(textNode => textNode.id === textNodeIndex)
  textElement.innerText = textNode.text
  while (valgKnapperElement.firstChild) {
    valgKnapperElement.removeChild(valgKnapperElement.firstChild)
  }

  textNode.valg.forEach(valg => {
    if (visValg(valg)) {
      const button = document.createElement('button')
      button.innerText = valg.text
      button.classList.add('btn')
      button.addEventListener('click', () => velgValg(valg))
      valgKnapperElement.appendChild(button)
    }
  })
}

function visValg(valg) {
  return valg.requiredStart == null || valg.requiredStart(start)
}

// if setninger for hva som skjer når nexTextNodeId er et spesifikt tall, eksempelvis skal musikk osv. spilles av
function velgValg(valg) {
  const nextTextNodeId = valg.nextText
  if (nextTextNodeId == -1) {
    restartLyd.play();
    return startSpill();
  }
  else if(nextTextNodeId == 20 || nextTextNodeId == 22){
    winLyd.play();
  }
  else if(nextTextNodeId == 2) {
    backgroundmusic.play();
  }
  else if(nextTextNodeId >= 0) {
    knappLyd.play();
  }
  else if (nextTextNodeId == -2) {
  window.location.replace("./database.html")
  }
  
  start = Object.assign(start, valg.setStart)
  visTextNode(nextTextNodeId)
}

//Her er all teksten og valgene man kan ta
const textNodes = [
  {
    id: 1,
    text: 'Trykk her for å begynne spillet', //Overskriften for valget
    valg: [ //De ulike valgene man kan ta
      {
        text: 'Start spillet', //Tekst for et valg man kan ta
        nextText: 2 //Refererer til neste id hvis man trykker på denne knappen
      },
    ]
  },
  {
    id: 2,
    text: 'Du våkner opp i et slags fengsel i et romskip og husker ikke hvordan du kom dit. Du ser en vakt utenfor fengselet. Hva gjør du?',
    valg: [
      {
        text: 'Bestikker vakten med godteri',
        nextText: 3
      },
      {
        text: 'Prøver å rømme igjennom ventilasjonssystemet',
        nextText: 4
      },
      {
        text: 'Blir værende i romskipet for resten av livet',
        nextText: 5
      }
    ] 
  },
  {
    id: 3,
    text: 'Vakten liker godteriet ditt og lar deg komme ut av fengselet. Nå er han på laget ditt. Hva gjør du nå?',
    valg: [
      {
        text: 'Du tar på deg klærne hans og later som om du er et romvesen',
        nextText: 6
      },
      {
        text: 'Du liker ikke å være på lag med noen, og slår dermed vakten ned',
        nextText: 7
      }
    ]
  },
  {
    id: 4,
    text: 'Ventilasjonssystemet er for trangt, men det er en mulighet å rømme igjennom. Hva gjør du?',
    valg: [
      {
        text: 'Du prøver å ikke spise noen ting for å bli tynnere for å kunne krype igjennom ventilasjonssystemet',
        nextText: 8
      },
      {
        text: 'Du dropper det allikevel og blir lenger i fengselet for å finne ut en bedre plan',
        nextText: 9
      }

    ]
  },
  {
    id: 5,
    text: 'Du dør etterhvert av romvesner som tydeligvis hadde fanget deg for å studere og deretter drepe deg.',
    valg: [
      {
        text: 'Restart',
        nextText: -1
      }
    ]
  },
  {
    id: 6,
    text: 'De andre vaktene legger ikke merke til at du ikke er en vakt. Hvor går du videre?',
    valg: [
      {
        text: 'I vaktrommet for å slå av alle kameraer',
        nextText: 10
      },
      {
        text: 'Går ut av romskipet',
        nextText: 11
      },
      {
        text: 'Prøver å skyte alle i skipet med våpenet til vakten',
        nextText: 12
      }
    ]
  },
  {
    id: 7,
    text: 'Bra jobbet! Du kan ikke stole på noen i verdensrommet. Du ser tre dører foran deg. Hvilke av de velger du?',
    valg: [
      {
        text: 'Dør med dødningssymbol',
        nextText: 13
      },
      {
        text: 'Dør med regnbuesymbol',
        nextText: 14
      },
      {
        text: 'Dør med nøkkelsymbol',
        nextText: 14
      }
    ]
  },
  {
    id: 8,
    text: 'Du dør dessverre av sultmangel',
    valg: [
      {
        text: 'Restart',
        nextText: -1
      }
    ]
  },
  {
    id: 9,
    text: 'Du blir gal av å være i fengselet og dør i fengselet',
    valg: [
      {
        text: 'Restart',
        nextText: -1
      }
    ]
  },
  {
    id: 10,
    text: 'Det er veldig avansert teknologi i rommet, men heldigvis har du gått IT. Hvordan går du frem for å slå av kameraene?',
    valg: [
      {
        text: 'Du trykker på den røde knappen',
        nextText: 13
      },
      {
        text: 'Du hacker deg igjennom main framen og slår av kameraene',
        nextText: 15
      },
      {
        text: 'Du bruker våpenet ditt for å ødelegge alt i rommet',
        nextText: 16

      }
    ]
  },
  {
    id: 11,
    text: 'Vaktens klær er ikke laget for utenfor romskipet så du dør av oksygenmangel',
    valg: [
      {
        text: 'Restart',
        nextText: -1
      }
    ]
  },
  {
    id: 12,
    text: 'Du skyter alle på din vei, men når du kommer til hovedrommet er det hundrevis av vakter der. Hva gjør du?',
    valg: [
      {
        text: 'Du fortsetter å skyte alle du ser',
        nextText: 17
      },
      {
        text: 'Du løper tilbake igjen',
        nextText: 18
      },
      {
        text: 'Du gir opp og står stille',
        nextText: 19
      }
    ]
  },
  {
    id: 13,
    text: 'Her ser du et nytt romskip. Hva gjør du?',
    valg: [
      {
        text: 'Drar hjem til jorden',
        nextText: 20
      },
      {
        text: 'Du tør ikke og blir værende på romskipet for resten av livet',
        nextText: 5
      }
    ]
  },
  {
    id: 14,
    text: 'Regnbuedøren og nøkkeldøren leder til samme rom. Her er alle nøklene til alle rom på skipet, men rommet er svært overvåket. Hva gjør du?',
    valg: [
      {
        text: 'Går ut av rommet igjen',
        nextText: 21
      },
      {
        text: 'Stjeler noen nøkler for å komme deg ut av romskipet',
        nextText: 21
      },
      {
        text: 'Ødelegger kameraene i rommet',
        nextText: 21
      }
    ]
  },
  {
    id: 15,
    text: 'Med dine IT-skills klarer du dette og tar over skipet. Hva gjør du?',
    valg: [
      {
        text: 'Du flyr hjem til jorden',
        nextText: 20
      },
      {
        text: 'Du blir den nye stjernehelten i universet',
        nextText: 22
      }
    ]
  },
  {
    id: 16,
    text: 'Romskipet krasjer fordi du knuste alle kontrollene i skipet',
    valg: [
      {
        text: 'Restart',
        nextText: -1
      }
    ]
  },
  {
    id: 17,
    text: 'Det er altfor mange romvesen, så du dør',
    valg: [
      {
        text: 'Restart',
        nextText: -1
      }
    ]
  },
  {
    id: 18,
    text: 'På veien tilbake finner du en ødelagt robot. Hva gjør du?',
    valg: [
      {
        text: 'Programmerer den til å skyte vaktene',
        nextText: 23
      },
      {
        text: 'Lar den være',
        nextText: 24
      }
    ]
  },
  {
    id: 19,
    text: 'Du dør av at de skyter deg',
    valg: [
      {
        text: 'Restart',
        nextText: -1
      }
    ]
  },
  {
    id: 20,
    text: 'Gratulerer! Du overlevde og kom deg trygt tilbake igjen til jorden.',
    valg: [
      {
        text: 'Restart',
        nextText: -1
      },
      {
        text: 'Registrer deg',
        nextText: -2
      }
    ]
  },
  {
    id: 21,
    text: 'Du ble oppdaget, og døde dessverre',
    valg: [
      {
        text: 'Restart',
        nextText: -1
      }
    ]
  },
  {
    id: 22,
    text: 'Gratulerer! Nå kaller alle deg "Star Lord"',
    valg: [
      {
        text: 'Restart',
        nextText: -1
      },
      {
        text: 'Registrer deg',
        nextText: -2
      }
    ]
  },
  {
    id: 23,
    text: 'Med dine IT-skills får du til dette, men roboten blir etterhvert ødelagt og du dør',
    valg: [
      {
        text: 'Restart',
        nextText: -1
      }
    ]
  },
  {
    id: 24,
    text: 'Bra valg, fordi den var så og si ødelagt. Du løper nå igjennom gangen og ser et romskip i et rom. Hva gjør du?',
    valg: [
      {
        text: 'Du går inn i skipet og prøver å fly hjem til jorden',
        nextText: 25
      },
      {
        text: 'Lar den være',
        nextText: 26
      }
    ]
  },
  {
    id: 25,
    text: 'Romskipet var ødelagt, så du dør dessverre',
    valg: [
      {
        text: 'Restart',
        nextText: -1
      }
    ]
  },
  {
    id: 26,
    text: 'Bra valg, fordi den var også ødelagt. Dessverre så er du nå i en blindvei og alle romvesnene er etter deg, så du dør',
    valg: [
      {
        text: 'Restart',
        nextText: -1
      }
    ]
  }
]

// Starter funksjonen slik at spillet starter
startSpill()