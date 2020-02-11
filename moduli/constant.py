"""
Modul u kome se nalaze konstante.
"""
import numpy as np 
import pygame 
import sys

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
TAMNO_SIVA = (117, 117, 117)
CRNA = (0,0,0)
ZUTA = (255,255,0)
red = (200,0,0)
green = (0,200,0)

bright_red = (255,0,0)
bright_green = (0,255,0)

VELICINA_KVADRATA = 90
PROSTOR_ZA_SLIKU = 240
width = BROJ_KOLONA * VELICINA_KVADRATA
height = (BROJ_REDOVA+1) * VELICINA_KVADRATA 
size = (width, height+ PROSTOR_ZA_SLIKU)
RADIUS = int(VELICINA_KVADRATA/2 - 5)
screen = pygame.display.set_mode(size)


pygame.init()
myfont = pygame.font.SysFont("monospace", 55)
fontZaButtn = pygame.font.SysFont("monospace", 20)