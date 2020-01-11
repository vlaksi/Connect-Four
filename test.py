import numpy as np 
import pygame 
import sys
import math
import random

PLAYER = 0
AI = 1
PRAZNO_POLJE = 0
PLAYER_TOKEN = 1
AI_TOKEN = 2

BROJ_REDOVA = 6
BROJ_KOLONA = 6
POVRSINA_ZA_POBEDU = 4

BELA = (255,255,255)
SIVA = (200,200,200)
CRNA = (0,0,0)
ZUTA = (255,255,0)

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

#F-ja koja vrsi renderovanje GUI-a tj prikaz nase igre
def iscrtaj_tablu(tabla):
	for c in range(BROJ_KOLONA):
		for r in range(BROJ_REDOVA):
			pygame.draw.rect(screen, BELA, (c*VELICINA_KVADRATA, r*VELICINA_KVADRATA+VELICINA_KVADRATA, VELICINA_KVADRATA, VELICINA_KVADRATA))
			pygame.draw.circle(screen, SIVA, (int(c*VELICINA_KVADRATA+VELICINA_KVADRATA/2), int(r*VELICINA_KVADRATA+VELICINA_KVADRATA+VELICINA_KVADRATA/2)), RADIUS)
	
	for c in range(BROJ_KOLONA):
		for r in range(BROJ_REDOVA):		
			if tabla[r][c] == PLAYER_TOKEN:
				pygame.draw.circle(screen, ZUTA, (int(c*VELICINA_KVADRATA+VELICINA_KVADRATA/2), height - int(r*VELICINA_KVADRATA+VELICINA_KVADRATA/2)), RADIUS)
			elif tabla[r][c] == AI_TOKEN:
				pygame.draw.circle(screen, CRNA, (int(c*VELICINA_KVADRATA+VELICINA_KVADRATA/2), height - int(r*VELICINA_KVADRATA+VELICINA_KVADRATA/2)), RADIUS)
	pygame.display.update()


#F-ja koja daje bodove celijama nase tabele
def proceni_povrsinu_za_pobedu(povrsina_za_pobedu, token):
	score = 0
	protivnicki_token = PLAYER_TOKEN
	if token == PLAYER_TOKEN:
		protivnicki_token = AI_TOKEN

	if povrsina_za_pobedu.count(token) == 4:
		score += 100
	elif povrsina_za_pobedu.count(token) == 3 and povrsina_za_pobedu.count(PRAZNO_POLJE) == 1:
		score += 5
	elif povrsina_za_pobedu.count(token) == 2 and povrsina_za_pobedu.count(PRAZNO_POLJE) == 2:
		score += 2

	if povrsina_za_pobedu.count(protivnicki_token) == 3 and povrsina_za_pobedu.count(PRAZNO_POLJE) == 1:
		score -= 4

	return score

#F-ja koja vrsi bodovanje 
def score_position(tabla, token):
	score = 0

	## Boduj horizontalno
	for r in range(BROJ_REDOVA):
		red_array = [int(i) for i in list(tabla[r,:])]
		for c in range(BROJ_KOLONA-3):
			povrsina_za_pobedu = red_array[c:c+POVRSINA_ZA_POBEDU]
			score += proceni_povrsinu_za_pobedu(povrsina_za_pobedu, token)

	return score


tabla = kreiraj_tablu()
game_over = False

# Konfigurisanje GUI-a
pygame.init()
VELICINA_KVADRATA = 90
width = BROJ_KOLONA * VELICINA_KVADRATA
height = (BROJ_REDOVA+1) * VELICINA_KVADRATA
size = (width, height)
RADIUS = int(VELICINA_KVADRATA/2 - 5)
screen = pygame.display.set_mode(size)

iscrtaj_tablu(tabla)
pygame.display.update()

myfont = pygame.font.SysFont("monospace", 55)

turn = random.randint(PLAYER, AI)

while not game_over:

	# Prolazak kroz Event Lisenere od koristi i njihova implementacija
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.MOUSEMOTION:
			pygame.draw.rect(screen, BELA, (0,0, width, VELICINA_KVADRATA))
			posx = event.pos[0]
			if turn == PLAYER:
				pygame.draw.circle(screen, ZUTA, (posx, int(VELICINA_KVADRATA/2)), RADIUS)
			
		pygame.display.update()

		if event.type == pygame.MOUSEBUTTONDOWN:
			pygame.draw.rect(screen, BELA, (0,0, width, VELICINA_KVADRATA))

			if turn == PLAYER:
				# normalizujemo poziciju, tj kako bi na osnovu piksela 641,dobili da je to 6 kolona recimo.
				posx = event.pos[0]
				kolona = int(math.floor(posx/VELICINA_KVADRATA)) 

				if da_li_je_popunjena_kolona(tabla,kolona):
					red = get_sledeci_slobodan_red(tabla,kolona)
					postavi_token(tabla,red,kolona,PLAYER_TOKEN)

					if winning_move(tabla,PLAYER_TOKEN):
						label = myfont.render("POBEDA ZUTOG !!", 1, ZUTA)
						screen.blit(label, (10,5))
						game_over = True

					stampaj_tablu(tabla)
					iscrtaj_tablu(tabla)
					# prelazak na sledeceg igraca
					turn += 1
					turn = turn % 2

	if turn == AI and not game_over:	
		kolona = random.randint(0,BROJ_KOLONA-1)

		if da_li_je_popunjena_kolona(tabla,kolona):
			pygame.time.wait(700);
			red = get_sledeci_slobodan_red(tabla,kolona)
			postavi_token(tabla,red,kolona,AI_TOKEN)

			if winning_move(tabla,AI_TOKEN):
				label = myfont.render("POBEDA CRNOG !!", 1, CRNA)
				screen.blit(label, (10,5))
				game_over = True

			stampaj_tablu(tabla)
			iscrtaj_tablu(tabla)
			# prelazak na sledeceg igraca
			turn += 1
			turn = turn % 2

	# Iskljucivanje igre nakon game_overa-a
	if game_over:
		pygame.time.wait(3000)