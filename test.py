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

#F-ja koja odredjuje da li je odigrani potez pobednicki
def winning_move(tabla,token):
	# proveri horizontalne lokacije
	for c in range(BROJ_KOLONA-3):
		for r in range(BROJ_REDOVA):
			if tabla[r][c] == token and tabla[r][c+1] == token and tabla[r][c+2] == token and tabla[r][c+3] == token:
				return True

	# proveri vertikalne lokacije
	for c in range(BROJ_KOLONA):
		for r in range(BROJ_REDOVA-3):
			if tabla[r][c] == token and tabla[r+1][c] == token and tabla[r+2][c] == token and tabla[r+3][c] == token:
				return True

	# proveri lokacije na glavnoj dijagonali 
	for c in range(BROJ_KOLONA-3):
		for r in range(BROJ_REDOVA-3):
			if tabla[r][c] == token and tabla[r+1][c+1] == token and tabla[r+2][c+2] == token and tabla[r+3][c+3] == token:
				return True

	#proveri lokacije na sporednoj dijagonali
	for c in range(BROJ_KOLONA-3):
		for r in range(3, BROJ_REDOVA):
			if tabla[r][c] == token and tabla[r-1][c+1] == token and tabla[r-2][c+2] == token and tabla[r-3][c+3] == token:
				return True

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

			if winning_move(tabla,1):
				print("IGRAC 1 je POBEDNIK !!!")
				game_over = True

	# Ponudi unos drugom igracu
	else:
		kolona = int(input("Igracu 2, unesite vasu kolonu (0-6):"))
		if da_li_je_popunjena_kolona(tabla,kolona):
			red = get_sledeci_slobodan_red(tabla,kolona)
			postavi_token(tabla,red,kolona,2)

			if winning_move(tabla,2):
				print("IGRAC 2 je POBEDNIK !!!")
				game_over = True

	stampaj_tablu(tabla)
	# prelazak na sledeceg igraca, matematicki da uvek bude izmedju 0-1
	turn += 1
	turn = turn % 2