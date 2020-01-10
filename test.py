import numpy as np 

BROJ_REDOVA = 6
BROJ_KOLONA = 6


#F-ja koja kreira matricu 6 puta 6, koja predstavlja tablu
def kreiraj_tablu():
	tabla = np.zeros((BROJ_REDOVA,BROJ_KOLONA))
	return tabla

tabla = kreiraj_tablu()
game_over = False
turn = 0

while not game_over:
	# Ponudi unos prvom igracu
	if turn == 0:
		selection = int(input("Igracu 1, unesite vasu kolonu (0-6):"))

	# Ponudi unos drugom igracu
	else:
		selection = int(input("Igracu 2, unesite vasu kolonu (0-6):"))