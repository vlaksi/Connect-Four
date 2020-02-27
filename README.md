<h1 align = "center"> Nacin pokretanja </h1>

## Requiremets
<p align = "left">

Kako bi preuzeli igru, mozete jednostavno klonirati repozitorijum na vasem racunaru, ili skinuti zipovan projekat. Kako bi instalirali sve biblioteke i pokrenuli igru pomocu nekog od okruzenja koje podrzava Python, morate uraditi sledece.

  - Pozicionirate se gde se nalazi nasa igra, tacnije folder requirements.txt
  - Otvorite tu cmd i ukucate sledece:
  ```sh
$ pip install -r requirements.txt
```

## Pokretanje aplikacije
Potrebno je da se pozicionirate u okvir direktorijuma vas_path/Connect-Four/ koji ste prethodno skinuli/klonovali. A potom na sledeci nacin mozete pokrenuti aplikaciju:
```sh
$ python igra.py
```

 </p>


<h1 align = "center"> Nacin igranja </h1>
<p align = "left">
  
Igranje je vrlo intuitivno, pomeranjem misa levo desno mozete da izaberete kolonu u koju zelite da spustite token(ZETON), klikom na kolonu automatski ce se popuniti prvi slobodan red sa zetonom, zatim je na redu implementirani AI algoritam i tako nazimenicno se smenjujte. Ko ce biti prvi na potezuje AI ili Vi, o tome odlucuje RANDOM generator. 
  
  </p>
