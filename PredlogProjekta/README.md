# Numericki-algoritmi-i-numericki-softver-PREDLOG-PROJEKTA


 <h1 align="center"> Interaktivna igra connect four 
</h1>

<p align="center">
  <img width="300" height="200" src="https://cf.geekdo-images.com/itemrep/img/PlGbhfaxgidPGU_jPO0ccr8vPBc=/fit-in/246x300/pic738020.jpg">
</p>

<h1> Uvod </h1>
<p align = "left">
  
Connect four (poznata i kao Kapetanova ljubavnica, Cetiri gore, Plot Cetiri, Pronadji cetvorku, Cetiri u nizu, Cetiri u redu, Pusti cetvorku i Gravitrips (u Sovjetskom Savezu)) je igra za povezivanje sa dva igraca u kojoj igraci prvo izaberu boju, a zatim se okrecu tako sto ce jednobojni disk s vrha prebaciti u vertikalno okacenu resetku sa sest stupaca. Komadi padaju ravno dole, zauzimajuci najnizi raspolozivi prostor u koloni. Cilj igre je biti prvi koji ce formirati horizontalnu, vertikalnu ili dijagonalnu liniju od cetiri sopstvena diska. Connect Four je resena igra. Prvi igrac uvek moze pobediti igrajuci prave poteze.


Primer igranja, prvi igrac koji zapocinje Connect Four bacajuci jedan od njihovih zutih diskova u neki od 7 stupaca prazne table za igru. Dvojica igraca zatim naizmenicno igraju spustajuci jedan od svojih diskova u nepopunjenu kolonu, sve dok neki igrac, ne postigne dijagonalu cetiri zaredom i pobedi u igri. Za igre u kojima se tabla popuni pre nego sto bilo koji igrac postigne cetiri u nizu, tada su igre neresene.

<div>
  <p align="right">
    <img width="800" height="320" src="https://static.packt-cdn.com/products/9781788834247/graphics/B09471_18_02.jpg">
  </p>
</div>


Connect Four je igra za dva igraca sa "savrsenim informacijama". Ovaj izraz opisuje igre u kojima jedan igrac u datom trenutku igra, igraci imaju sve informacije o potezima koji su se odigrali i svim potezima koji se mogu dogoditi, za odredjeno stanje igre. Connect Four takodje pripada klasifikaciji protivnicke igre sa nultom sumom, jer prednost igraca predstavlja protivnikov nedostatak. Jedna mera slozenosti igre Connect Four je broj mogucih pozicija na tabli za igre. Za klasicni Connect Four koji se igra na 6 visokih, 7 sirokih resetki, postoji 4.531.985.219.092 pozicija za sve table za igru popunjene od 0 do 42 komada.

Connect Four je od tada resen grubim metodama, pocevsi od rada Dzona Trompa na sastavljanju 8-slojne baze podataka. Algoritmi za vestacku inteligenciju koji mogu snazno da rese Connect Four su minimaks ili negamaks, sa optimizacijama koje ukljucuju alfa-beta obrezivanje, naredjivanje pomeranja i tablice prenosa.
</p>

<h1> Minmaks algoritam </h1>

<p align = "left">
 
Minimaks algoritam je rekurzivni algoritam za odabir sledeceg poteza u n-igraca igrama, uglavnom za dva igraca. Vrednost je povezana sa svakom pozicijom ili stanjem igre. Ova vrednost se izracunava pomocu funkcije evaluacije pozicije i pokazuje koliko ta pozicija moze znaciti igracima.
  

Igrac onda pravi potez koji maksimizuje minimalnu vrednost polozaja protivnikovih mogucih poteza. Ako se A pokrenuo, A daje vrednost svakom od njegovih legalnih poteza. Moguca alokacija metoda se sastoji iz dodeljivanja pobede za A kao +1 i za B kao -1. Alternativno koriscenje pravila je ako je rezultat poteza pobeda za A dodeljuje se pozitivna beskonacnost i, ako je rezultat pobeda za B, dodeljuje se negativna beskonacnost.

Vrednost A bilo kog sledeceg poteza je minimum vrednosti koje su nastale od svakog od B's mogucih odgovora. Iz ovog razloga, A zovemo maximizing player i B zovemo minimizing player, otuda naziv minimaks algoritam.

<div>
  <p align="center">
    <img width="500" height="350" src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Minimax.svg/400px-Minimax.svg.png">
  </p>
</div>

Ovo moze biti **prosireno** ako mozemo da pruzimo heuristicnu evaluaciju funkcija koje dodeljuju vrednosti nezavrsnom potezu bez uzimanja u obzir sve mogucnosti pratecih kompletnih sekvenci. Tako mozemo ograniciti minimaks algoritam tako sto gledamo samo odredjeni broj poteza napred. Ovaj broj se zove "look-ahead", meren u "plies (Ply (chess))".

Algoritam se moze posmatrati kao istrazivanje cvorova (node (computer science)) kod drveta igara (game tree). Efikasan faktor grananja (branching factor) drveta je srednja vrednost dete cvora svakog cvora (tj. srednja vrednost legalnih poteza na poziciju). Broj cvorova koji se uglavnom istrazuju se povecavaju eksponencijalno (exponential growth) sa brojem slojeva(manje je od eksponencijalnog ako se evaluira grub potez ili ponavljanje pozicija).

Broj cvorova koji se istrazuju za analize igre je ,dakle, priblizno faktor grananja povecao do jacine broja slojeva. On je  nepraktican (Computational complexity theory#Intractability) da bi se zavrsila analiza igara kao sto je sah koristeci minimaks algoritam. Performanse naivnog minimaks algoritma mogu biti dramaticno unapredjene, bez odrazavanja na rezultat, koristeci **alfa-beta pretragu**.


Ostale heuristicke metode mogu ,takodje, da se koriste, ali ne moze se za sve njih garantovati da ce dati rezultate kao nepromenjena pretraga.
</p>

<h1> Upotreba numerickih metoda </h1>

<p align ="left">
 
 <div>
  <p align="center">
    <img width="1000" height="340" src="https://img.deusm.com/darkreading/1331840_Slideshow/Slide1CoverArt.jpg">
  </p>
</div>
 
 Nas najveci problem se zasniva na odredjivanju verovatnoce pobede protiv racunara koji je naucen da igra perfektno i bez premca uvek moze da nas pobedi. Ta verovatnoca treba da nam pomogne da odredimo u koju kolonu treba da stavimo token tako da bi verovatnoca pobede bila na nasoj strani i uvek bila sto veca. Ideja je zasnovana na tome da mi imamo algoritam koji je zasnovan na nekoj od numerckih metoda koji ce da sluzi kao nas mali pomocnik.
 
 Istrazivanja su pokazala da najbolje rezultate ne daje AI, isto tako najbolje rezultate ne daje ni covek, najbolje rezultate dobijamo kada se udruze snage coveka i vestacke inteligencije.
 U tome nam trebaju pomoci neke od numerickih metoda [Interpolacija](https://github.com/vlaksi/NAiNS/tree/master/vezbe%5Bzadaci%5D/v5) , Regresija i druge.

 Izazov ce biti i napraviti Data Set koji ce po mogucnosti biti sto veci kako bi nam metode sto bolje  pomogle u nasem pokusaju savladavanja racunara. Data Set ce biti generisan na osnovu prethodnih odigranih partija koje imamo u planu da zabelezimo u csv ili nekom slicnom formatu, zatim da sve to transformisemo u tabele. Data Set ce biti osnov za to da numericke metode daju validnu predikciju. 
 
 
 <div>
  <p align="center">
    <img width="1000" height="320" src="http://cdn7.dissolve.com/p/D873_157_002/D873_157_002_0004_600.jpg">
  </p>
</div>
 
 
 </p>


<h1> Nacin izrade projekta </h1>

<p align="left">
  
Projekat planiramo da realizujemo na osnovu **SCRUM** metodologije i tehnologija koje budu relevantne za nase zahteve u projektu.
Nas tim bi pokusao da odrzi par *sprintova* u kojima bi posle svakog sprinta imao odredjeni produkt koji ce biti dostupan na GitHub-u.
### Sprint 1
###### Plan:  ***tabla igre i funkcionalnost igranja pvp*** <br /> Izrada: Koriscenje raznih tehnologija implementiranih u kod <br /> Test: zajednickim snagama pokusavamo da otkrijemo bagove tokom izrade <br /> Prikaz: na odgovarajucem repozitorijumu

### Sprint 2
###### Plan:  ***implementiranje AI minmax i verovatnoce pobede*** <br /> Izrada: Koriscenje raznih tehnologija implementiranih u kod <br /> Test: zajednickim snagama pokusavamo da otkrijemo bagove tokom izrade <br /> Prikaz: na odgovarajucem repozitorijumu
### Sprint 3
###### Plan:  ***implementirana fizika prilikom pada tokena na tlo*** <br /> Izrada: Implementacija fizike <br /> Test: zajednickim snagama pokusavamo da otkrijemo bagove tokom izrade <br /> Prikaz: na odgovarajucem repozitorijumu
### Sprint 4
Ako nam vreme dozvoli ovaj sprint bi posvetili *optimizacija koda,igre i grafike*. <br />
#### Product Owner
Product owner bi bio nas asistent i mentor [Ognjen Francuski](https://www.linkedin.com/in/ognjen-francuski-6b02a581/?locale=de_DE) 
#### Scrum Master i Tim
Nas tim bi bio i tim i Scrum Master sadrzan od : ***Ane Perisic RA1/2017, Nemanje Pualica RA162/2017 i Vladislava Maksimovica RA186/2017*** .



 <div>
  <p align="center">
    <img width="350" height="160" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQnaMBzqmOyz61p6jP8ze8UkcDqK6hU_PVj57Kx-_QkAD_c_CEj&s">
  </p>
</div>

</p>


<h1> Literatura i materijali </h1>
<p align = "left">
 
 
   #### Literatura
   MIT 6.034 Artificial Intelligence: https://www.youtube.com/watch?v=STjW3eH0Cik&t=1494s <br /> https://de.wikipedia.org/wiki/Minimax-Algorithmus <br /> https://www.javatpoint.com/mini-max-algorithm-in-ai <br /> https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-1-introduction/ <br /> https://www.pygame.org/docs/ <br /> https://stackoverflow.com <br /> Materijali sa vezbi i predavanja <br />
  
  
  <div>
  <p align="center">
    <img width="1000" height="320" src="https://www.historic-uk.com/wp-content/uploads/2018/11/edwardian-literature-2800x1440.jpg">
  </p>
</div>
  
  
  #### Primeri gotovih resenja
  GitHub: <br />  https://github.com/loganbwu/Connect-Four <br />  https://github.com/RyanMarcus/connect4 <br />  https://github.com/codyseibert/js-connect-four <br />  https://github.com/KeithGalli/Connect4-Python <br />  https://github.com/ahmet2106/connect4-python <br /> 
  Test igre: <br />  https://www.youtube.com/watch?v=yDWPi1pZ0Po
  

  
</p> 








