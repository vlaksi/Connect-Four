import numpy as np 

BROJ_REDOVA = 6
BROJ_KOLONA = 6


#F-ja koja kreira matricu 6 puta 6, koja predstavlja tablu
def kreiraj_tablu():
	tabla = np.zeros((BROJ_REDOVA,BROJ_KOLONA))
	return tabla

#F-ja koja okrece nasu tablu, jer je u numpy biblioteci kord pocetak, u gonjem levom cosku
def stampaj_tablu(tabla):
	print(np.flip(tabla,0))

#F-ja koja postavlja token na odgovarajucu poziciju u matrici
def postavi_token(tabla,red,kolona,token):
	tabla[red][kolona] = token

#F-ja koja provera da li je validna lokacija, tj da li je 5 red prosledjene kolone slobodan
def da_li_je_popunjena_kolona(tabla, kolona):
	return tabla[BROJ_REDOVA-1][kolona] == 0

#F-ja koja vraca indeks prvog slobodnog reda
def get_sledeci_slobodan_red(tabla,kolona):
	for i in range(BROJ_REDOVA):
		if tabla[i][kolona] == 0:
			return i

tabla = kreiraj_tablu()
game_over = False
turn = 0

while not game_over:
	# Ponudi unos prvom igracu
	if turn == 0:
		kolona = int(input("Igracu 1, unesite vasu kolonu (0-6):"))

		if da_li_je_popunjena_kolona(tabla,kolona):
			red = get_sledeci_slobodan_red(tabla,kolona)
			postavi_token(tabla,red,kolona,1)
	# Ponudi unos drugom igracu
	else:
		kolona = int(input("Igracu 2, unesite vasu kolonu (0-6):"))
		if da_li_je_popunjena_kolona(tabla,kolona):
			red = get_sledeci_slobodan_red(tabla,kolona)
			postavi_token(tabla,red,kolona,2)

	stampaj_tablu(tabla)
	# prelazak na sledeceg igraca, matematicki da uvek bude izmedju 0-1
	turn += 1
	turn = turn % 2