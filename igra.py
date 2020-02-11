import numpy as np 
import pygame 
import sys
import math
import random
import ctypes
import imageio
import csv
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib
from matplotlib.pylab import rcParams
from sklearn.datasets import load_boston
#from sklearn.cross_validation import train_test_split
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
import ctypes
import easygui
import random
import tkinter as tk
from tk_html_widgets import HTMLLabel
from threading import Thread, Event
import time

while (1):
    gameMode = easygui.enterbox("Unesite 1 ili 2 (mod 1 je mod u kom AI igra po MINMAX algoritmu, mod 2 je mod u kom AI igra po predikciji numerike na osnovu istreniranog dataseta  ")
    if(gameMode == '1' or gameMode == '2'):
        break

rcParams['figure.figsize'] = 8, 6
matplotlib.rcParams.update({'font.size': 12})

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

# Event objekat koji sluzi da salje signale od jedne do druge niti
stop_event = Event()

# F-j koja implementira spustanje tokena. Ceka 5 sekundi u kojima se vrsi simulacija fizike.
def spusti_token(red,kolona,boja):
    # Od gornjeg dela do reda u kom smo vrsimo spustanje tokena.
    for i in range(5,red,-1):
        pygame.draw.circle(screen, boja, (int(kolona*VELICINA_KVADRATA+VELICINA_KVADRATA/2), height - int((i*VELICINA_KVADRATA+VELICINA_KVADRATA/2))), RADIUS)
        pygame.display.update()
        time.sleep(0.020)
        if i != red:
            pygame.draw.circle(screen, SIVA, (int(kolona*VELICINA_KVADRATA+VELICINA_KVADRATA/2), height - int(i*VELICINA_KVADRATA+VELICINA_KVADRATA/2)), RADIUS)
            pygame.display.update()
            time.sleep(0.00001)

    # Simuliramo skakutanje naseg tokena u zavisnosti od reda.
    if red == 0 or red == 1 or red == 2:
        for i in range(red,3+red,1):
            skaci(boja,i,kolona)
        for i in range(3+red,red,-1):
            skaci(boja,i,kolona)
        for i in range(red,2+red,1):
            skaci(boja,i,kolona)
        for i in range(2+red,red,-1):
            skaci(boja,i,kolona)
        for i in range(red,1+red,1):
            skaci(boja,i,kolona)
        for i in range(1+red,red,-1):
            skaci(boja,i,kolona)
    if red == 3:
        for i in range(red,2+red,1):
            skaci(boja,i,kolona)
        for i in range(2+red,red,-1):
            skaci(boja,i,kolona)
        for i in range(red,1+red,1):
            skaci(boja,i,kolona)
        for i in range(1+red,red,-1):
            skaci(boja,i,kolona)


# F-ja za simulaciju skakanja.
def skaci(boja,i,kolona):
    pygame.draw.circle(screen, boja, (int(kolona*VELICINA_KVADRATA+VELICINA_KVADRATA/2), height - int((i*VELICINA_KVADRATA+VELICINA_KVADRATA/2))), RADIUS)
    pygame.display.update()
    time.sleep(0.1)
    pygame.draw.circle(screen, SIVA, (int(kolona*VELICINA_KVADRATA+VELICINA_KVADRATA/2), height - int(i*VELICINA_KVADRATA+VELICINA_KVADRATA/2)), RADIUS)
    pygame.display.update()
    time.sleep(0.00001)


# F-ja u kojoj pomocu niti vrsimo simulaciju fizike.
def fizika(red,kolona,boja):
    # Kreiramo novu nit
    action_thread = Thread(target=spusti_token,args=(red,kolona,boja))
 
    # I potom je pozivamo i damo joj maksimalno 5 sekundi da se izvrsi.
    action_thread.start()
    action_thread.join(timeout=5)
 
    # Dajemo signal ostalim nitima da sacekaju izvrsavanje nase niti.
    stop_event.set()
    #print("Hey there! I timed out! You can do things after me!")


# Dve liste koje sluze iscitavanje trainingSet kako bi vrsil numericke proracune nad njima
x = []
y = []
pom_y = []

# Iscitavanje iz fajla i smestanje u liste x i y
with open('trainingSet.csv', 'r') as csvfile:
    citac = csv.reader(csvfile, delimiter='\t')
    next(citac)
    for entitet in citac:
        x.append(int(entitet[0]))
        y.append(int(entitet[1]))

# Ispisivanje ucitanih lista
#print(x)
#print(y)

#F-ja koja kreira matricu 6 puta 6, koja predstavlja tablu
def kreiraj_tablu():
    tabla = np.zeros((BROJ_REDOVA,BROJ_KOLONA))
    return tabla

#F-ja koja okrece nasu tablu, jer je u numpy biblioteci kord pocetak, u gonjem levom cosku
def stampaj_tablu(tabla):
    print(np.flip(tabla,0))

# F-ja za simulaciju fizike
def bar():
    for i in range(100):
        print ("Tick")
        time.sleep(1)


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

    pygame.draw.rect(screen, BELA, (200,630, 500, 500))
    #Ucitavamo sliku
    myimage = pygame.image.load("picture/numerika.png")
    screen.blit(myimage, (0, 630)) #Parametri blit-a su slika, (xPozicija,yPozicija)
                                     #Blit je termin koji se koristi za renderovanje

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
        score -= 40

    return score

#F-ja koja vrsi bodovanje 
def score_position(tabla, token):
    score = 0

    ## Boduj centralnu kolonu
    center_array = [int(i) for i in list(tabla[:, BROJ_KOLONA//2])]
    centaralni_brojac = center_array.count(token)
    score += centaralni_brojac * 3

    ## Boduj horizontalno
    for r in range(BROJ_REDOVA):
        red_array = [int(i) for i in list(tabla[r,:])]
        for c in range(BROJ_KOLONA-3):
            povrsina_za_pobedu = red_array[c:c+POVRSINA_ZA_POBEDU]
            score += proceni_povrsinu_za_pobedu(povrsina_za_pobedu, token)

    ## Boduj vertikalno u pozitivno smeru(na gore)
    for c in range(BROJ_KOLONA):
        kolona_array = [int(i) for i in list(tabla[:,c])]
        for r in range(BROJ_REDOVA-3):
            povrsina_za_pobedu = kolona_array[r:r+POVRSINA_ZA_POBEDU]
            score += proceni_povrsinu_za_pobedu(povrsina_za_pobedu, token)

    ## Boduj vertiaklno u negativnom smeru(na dole)
    for r in range(BROJ_REDOVA-3):
        for c in range(BROJ_KOLONA-3):
            povrsina_za_pobedu = [tabla[r+i][c+i] for i in range(POVRSINA_ZA_POBEDU)]
            score += proceni_povrsinu_za_pobedu(povrsina_za_pobedu, token)

    for r in range(BROJ_REDOVA-3):
        for c in range(BROJ_KOLONA-3):
            povrsina_za_pobedu = [tabla[r+3-i][c+i] for i in range(POVRSINA_ZA_POBEDU)]
            score += proceni_povrsinu_za_pobedu(povrsina_za_pobedu, token)

    return score

#F-ja koja trazi sve validne(prazne) lokacije i smesta ih u niz,
# npr ako ako ni jedna kolona nije popunjena niz izgleda valid_location = [0,1,2,3,4,5]
def get_validne_lokacije(tabla):
    validne_lokacije = []
    for kolona in range(BROJ_KOLONA):
        if da_li_je_popunjena_kolona(tabla, kolona):
            validne_lokacije.append(kolona)
    return validne_lokacije

# F-ja koja vraca najpogodniju kolonu za odigrati potez
def izaberi_najbolji_potez(tabla, token):

    validne_lokacije = get_validne_lokacije(tabla)
    best_score = -10000
    best_kolona = random.choice(validne_lokacije)
    for kolona in validne_lokacije:
        red = get_sledeci_slobodan_red(tabla, kolona)
        temp_tabla = tabla.copy()
        postavi_token(temp_tabla, red, kolona, token)
        score = score_position(temp_tabla, token)
        if score > best_score:
            best_score = score
            best_kolona = kolona

    return best_kolona

def is_terminal_node(tabla):
    return winning_move(tabla, PLAYER_TOKEN) or winning_move(tabla, AI_TOKEN) or len(get_validne_lokacije(tabla)) == 0

def minimax(tabla, depth, alpha, beta, maximizingPlayer):
    validne_lokacije = get_validne_lokacije(tabla)
    is_terminal = is_terminal_node(tabla)
    if depth == 0 or is_terminal:
        if is_terminal:
            if winning_move(tabla, AI_TOKEN):
                return (None, 100000000000000)
            elif winning_move(tabla, PLAYER_TOKEN):
                return (None, -10000000000000)
            else: # Kraj igre, zato sto nema vise validnih poteza
                return (None, 0)
        else: # Depth is zero
            return (None, score_position(tabla, AI_TOKEN))
    if maximizingPlayer:
        value = -math.inf
        kolonaumn = random.choice(validne_lokacije)
        for kolona in validne_lokacije:
            red = get_sledeci_slobodan_red(tabla, kolona)
            b_copy = tabla.copy()
            postavi_token(b_copy, red, kolona, AI_TOKEN)
            new_score = minimax(b_copy, depth-1, alpha, beta, False)[1]
            if new_score > value:
                value = new_score
                kolonaumn = kolona
            alpha = max(alpha, value)
            if alpha >= beta:
                break

        return kolonaumn, value

    else: # Minimizing player
        value = math.inf
        kolonaumn = random.choice(validne_lokacije)
        for kolona in validne_lokacije:
            red = get_sledeci_slobodan_red(tabla, kolona)
            b_copy = tabla.copy()
            postavi_token(b_copy, red, kolona, PLAYER_TOKEN)
            new_score = minimax(b_copy, depth-1, alpha, beta, True)[1]
            if new_score < value:
                value = new_score
                kolonaumn = kolona
            beta = min(beta, value)
            if alpha >= beta:
                break

        return kolonaumn, value

def lasso_regression(data, predictors, alpha, models_to_plot={}):
    #Fit the model
    lassoreg = Lasso(alpha=alpha,normalize=True, max_iter=1e5)
    lassoreg.fit(data[predictors],data['y'])
    y_pred = lassoreg.predict(data[predictors])
    #print("Predikcija poteza", y_pred)
  
    #Return the result in pre-defined format
    rss = sum((y_pred-data['y'])**2)
    ret = [rss]
    ret.extend([lassoreg.intercept_])
    ret.extend(lassoreg.coef_)
    return ret

def ridge_regression(data, predictors, alpha):

    #Fit the model
    ridgereg = Ridge(alpha=alpha,normalize=True)
    ridgereg.fit(data[predictors],data['y'])
    y_pred = ridgereg.predict(data[predictors])
    #print("Predikcija poteza", y_pred)
    #print("PREDIKCIJA ZA PRVI POTEZ", y_pred[1])
   
    for p in y_pred:
        if p not in pom_y:
            pom_y.append(p)
    
    #for x in range(len(pom_y)):
    #    print("Predikcija za potez ", x+1 , round(abs(pom_y[x])))

    #Return the result in pre-defined format
    rss = sum((y_pred-data['y'])**2)
    ret = [rss]
    ret.extend([ridgereg.intercept_])
    ret.extend(ridgereg.coef_)
    return ret

def ridge_regression_PLOTOVANJE(data, predictors, alpha, models_to_plot={}):
    #Fit the model
    ridgereg = Ridge(alpha=alpha,normalize=True)
    ridgereg.fit(data[predictors],data['y'])
    y_pred = ridgereg.predict(data[predictors])

    #print("Predikcija poteza", y_pred)
    
    #Check if a plot is to be made for the entered alpha
    if alpha in models_to_plot:
        plt.subplot(models_to_plot[alpha])
        plt.tight_layout()
        plt.plot(data['x'],y_pred)
        plt.plot(data['x'],data['y'],'.')
        plt.title('Plot for alpha: %.3g'%alpha)
        plt.draw()
        plt.pause(1)

    #Return the result in pre-defined format
    rss = sum((y_pred-data['y'])**2)
    ret = [rss]
    ret.extend([ridgereg.intercept_])
    ret.extend(ridgereg.coef_)
    return ret

class DynamicArray(object): 
    #DYNAMIC ARRAY CLASS (Similar to Python List) 
    def __init__(self): 
        self.n = 0 # Count actual elements (Default is 0) 
        self.capacity = 1 # Default Capacity 
        self.A = self.make_array(self.capacity) 
          
    def __len__(self): 
        #Return number of elements sorted in array 
        return self.n 
      
    def __getitem__(self, k): 
        #Return element at index k 
        if not 0 <= k <self.n: 
            # Check it k index is in bounds of array 
            return IndexError('K is out of bounds !')  
          
        return self.A[k] # Retrieve from the array at index k 
          
    def append(self, ele): 
        #Add element to end of the array 
        if self.n == self.capacity: 
            # Double capacity if not enough room 
            self._resize(2 * self.capacity)  
          
        self.A[self.n] = ele # Set self.n index to element 
        self.n += 1
          
    def _resize(self, new_cap):  
        #Resize internal array to capacity new_cap 
        B = self.make_array(new_cap) # New bigger array 
          
        for k in range(self.n): # Reference all existing values 
            B[k] = self.A[k] 
              
        self.A = B # Call A the new bigger array 
        self.capacity = new_cap # Reset the capacity 
          
    def make_array(self, new_cap): 
        #Returns a new array with new_cap capacity 
        return (new_cap * ctypes.py_object)() 

tabla = kreiraj_tablu()
game_over = False

# Konfigurisanje GUI-a
pygame.init()
VELICINA_KVADRATA = 90
PROSTOR_ZA_SLIKU = 240
width = BROJ_KOLONA * VELICINA_KVADRATA
height = (BROJ_REDOVA+1) * VELICINA_KVADRATA 
size = (width, height+ PROSTOR_ZA_SLIKU)
RADIUS = int(VELICINA_KVADRATA/2 - 5)
screen = pygame.display.set_mode(size)

iscrtaj_tablu(tabla)
pygame.display.update()

myfont = pygame.font.SysFont("monospace", 55)
fontZaButtn = pygame.font.SysFont("monospace", 20)

turn = random.randint(PLAYER, AI)

indikator = -1
if turn == PLAYER:
    indikator = 1

# Inijalizacija dinamickog niza
nizPoteza = DynamicArray() 



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
                
            mouse = pygame.mouse.get_pos()
            #print(mouse)
            if 300+100 > mouse[0] > 300 and 650+50 > mouse[1] > 650:
                pygame.draw.rect(screen, TAMNO_SIVA,(300,650,160,50))
            else:
                pygame.draw.rect(screen, SIVA,(300,650,160,50))    

             #print(mouse)
            if 300+100 > mouse[0] > 300 and 725+50 > mouse[1] > 725:
                pygame.draw.rect(screen, TAMNO_SIVA,(300,725,160,50))
            else:
                pygame.draw.rect(screen, SIVA,(300,725,160,50))    

            if 300+100 > mouse[0] > 300 and 800+50 > mouse[1] > 800:
                pygame.draw.rect(screen, TAMNO_SIVA,(300,800,160,50))
            else:
                pygame.draw.rect(screen, SIVA,(300,800,160,50))   

            label1 = fontZaButtn.render("Pomoc", 1, CRNA)
            label2 = fontZaButtn.render("numerike", 1, CRNA)
            screen.blit(label1, (348,655)) #Prvi parametar x pozicija texta, drugi parametar y pozicija
            screen.blit(label2, (333,675))

            label3 = fontZaButtn.render("Princip", 1, CRNA)
            label4 = fontZaButtn.render("numerike", 1, CRNA)
            screen.blit(label3, (338,730)) #Prvi parametar x pozicija texta, drugi parametar y pozicija
            screen.blit(label4, (333,750))

            label5 = fontZaButtn.render("Training", 1, CRNA)
            label6 = fontZaButtn.render("data set", 1, CRNA)
            screen.blit(label5, (332,805)) #Prvi parametar x pozicija texta, drugi parametar y pozicija
            screen.blit(label6, (331,825))
        
          
            
        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, BELA, (0,0, width, VELICINA_KVADRATA))

            if 300+100 > mouse[0] > 300 and 800+50 > mouse[1] > 800:   
                x = sorted(x)         
                data = pd.DataFrame(np.column_stack([x,y]),columns=['x','y'])
                #plt.plot(data['x'],data['y'],'.')
                #plt.show()

                for i in range(2,16):  #power of 1 is already there
                    colname = 'x_%d'%i      #new var will be x_power
                    data[colname] = data['x']**i
                print (data.head())

                #Initialize predictors to be set of 15 powers of x
                predictors=['x']
                predictors.extend(['x_%d'%i for i in range(2,16)])

                #Set the different values of alpha to be tested
                alpha_ridge = [1e-15, 1e-10, 1e-8, 1e-4, 1e-3,1e-2, 1, 5, 10, 20]

                #Initialize the dataframe for storing coefficients.
                col = ['rss','intercept'] + ['coef_x_%d'%i for i in range(1,16)]
                ind = ['alpha_%.2g'%alpha_ridge[i] for i in range(0,10)]
                coef_matrix_ridge = pd.DataFrame(index=ind, columns=col)
                         
                models_to_plot = {1e-15:231, 1e-10:232, 1e-4:233, 1e-3:234, 1e-2:235, 5:236}
                for i in range(10):
                    coef_matrix_ridge.iloc[i,] = ridge_regression_PLOTOVANJE(data, predictors, alpha_ridge[i], models_to_plot)
                plt.show()

            if 300+100 > mouse[0] > 300 and 725+50 > mouse[1] > 725:
                root = tk.Tk()
                root.title("Ispod haube")

                html_label = HTMLLabel(root, html='<html><div><h1> ----------------- Princip numerike ----------------- </h1> <h4>Princip na kome radi numerika je zasnovan na regresiji i regulaciji. Metode koje koristimo su: Ridge i Lasso metoda takozvane L1 i L2 metode.<br><br>Nas program se samostalno trenira tokom kontinuiranog igranja, odnosno sto vise budemo igrali igru, dobijacemo bolje predikcije tj. savete koja kolona je najbolja da se odigra u sledecem potezu na osnovu naseg predjasnjeg iskustva u igranju protiv AI-a.<br> <br> Voditi racuna da MOD 2 nije optimalan na pocetku vaseg igranja, sto znaci da ce on tek postati kompetentan sa sve vecim vasim igranjem igre, zato sto se zasniva na podacima koje prikuplja od vaseg igranja protiv AI-a.<img src="picture/podaci.png"  width="600" height="350"><br><br>Kada nismo sigurni gde je najpametnije odigrati sledeci potez, nasa numerika ce tada izvrsiti regresiju i regulaciju i reci nam koji potez je optimalan.</h6> <h1> ---------------------- Metode ---------------------- </h1> <p> Metode koje uvode kaznenu funkciju tj. izraz zvan penal, a time koriguju izgled nase krive koja nam saopstava naredni potez su Lasso, Ridge metode. </p><img src="picture/Lm.png" width="600" height="100">  </div></html>')
                html_label.pack(fill="both", expand=True)
                html_label.fit_height()
                root.mainloop()


            if 300+100 > mouse[0] > 300 and 650+50 > mouse[1] > 650:     

                #Define input array with angles from 60deg to 300deg converted to radians
                #x = [1, 1,2 ,2,3,3,3,4,4,4,5,5,6,6,7,7,7,7,8,8,8,8,9,9,9,10,10,10,10,11,11,11,11,12,12,12,12,13,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]
                np.random.seed(10)  #Setting seed for reproducability
                #y = 4.5 + np.random.normal(0,1,len(x))
                data = pd.DataFrame(np.column_stack([x,y]),columns=['x','y'])
                for i in range(2,16):  #power of 1 is already there
                    colname = 'x_%d'%i      #new var will be x_power
                    data[colname] = data['x']**i

                #Initialize predictors to be set of 15 powers of x
                predictors=['x']
                predictors.extend(['x_%d'%i for i in range(2,16)])

                #Set the different values of alpha to be tested
                #alpha_ridge = [1e-15, 1e-10, 1e-8, 1e-4, 1e-3,1e-2, 1, 5, 10, 20]
                alpha_ridge = [1e-4]

                #Initialize the dataframe for storing coefficients.
                col = ['rss','intercept'] + ['coef_x_%d'%i for i in range(1,16)]
                ind = ['alpha_%.2g'%alpha_ridge[0]]
                coef_matrix_ridge = pd.DataFrame(index=ind, columns=col)

                models_to_plot = {1e-4:233}  
        
                coef_matrix_ridge.iloc[0,] = ridge_regression(data, predictors, alpha_ridge[0])

                if indikator==-1:
                    ctypes.windll.user32.MessageBoxW(0, "Pomoc"+ " numerike : U Vasem potezu " + str(len(nizPoteza)) + " po mom predjasnjem iskustvo najbolje je odigrati kolonu " + str(int(round(pom_y[len(nizPoteza)]))), "Predlog poteza", 4096)
                else:
                    ctypes.windll.user32.MessageBoxW(0, "Pomoc"+ " numerike : U Vasem potezu " + str(len(nizPoteza)+1) + " po mom predjasnjem iskustvo najbolje je odigrati kolonu " + str(int(round(pom_y[len(nizPoteza)+1]))), "Predlog poteza", 4096)
                
            
            if turn == PLAYER:

                if mouse[1] < 620:
                    # normalizujemo poziciju, tj kako bi na osnovu piksela 641,dobili da je to 6 kolona recimo.
                    posx = event.pos[0]
                    kolona = int(math.floor(posx/VELICINA_KVADRATA)) 

                    if da_li_je_popunjena_kolona(tabla,kolona):
                        red = get_sledeci_slobodan_red(tabla,kolona)
                        postavi_token(tabla,red,kolona,PLAYER_TOKEN)
                        fizika(red,kolona,ZUTA)
                        if winning_move(tabla,PLAYER_TOKEN):
                            label = myfont.render("POBEDA ZUTOG !!", 1, CRNA)
                            screen.blit(label, (10,5))
                            game_over = True

                        stampaj_tablu(tabla)
                        iscrtaj_tablu(tabla)
                        # prelazak na sledeceg igraca
                        turn += 1
                        turn = turn % 2

    if turn == AI and not game_over:    
        #kolona = random.randint(0,BROJ_KOLONA-1)
        #kolona = izaberi_najbolji_potez(tabla,AI_TOKEN)
        # Podesavanjem depth-a , tj drugog parametra uticemo na tezinu igre
        if(gameMode == '1'):
            kolona, minimax_score = minimax(tabla, 4, -math.inf, math.inf, True)
        else: 
            data = pd.DataFrame(np.column_stack([x,y]),columns=['x','y'])
            for i in range(2,16):  #power of 1 is already there
                colname = 'x_%d'%i      #new var will be x_power
                data[colname] = data['x']**i

            #Initialize predictors to be set of 15 powers of x
            predictors=['x']
            predictors.extend(['x_%d'%i for i in range(2,16)])

            #Set the different values of alpha to be tested
            #alpha_ridge = [1e-15, 1e-10, 1e-8, 1e-4, 1e-3,1e-2, 1, 5, 10, 20]
            alpha_ridge = [1e-4]

            #Initialize the dataframe for storing coefficients.
            col = ['rss','intercept'] + ['coef_x_%d'%i for i in range(1,16)]
            ind = ['alpha_%.2g'%alpha_ridge[0]]
            coef_matrix_ridge = pd.DataFrame(index=ind, columns=col)

            models_to_plot = {1e-4:233}  
    
            coef_matrix_ridge.iloc[0,] = ridge_regression(data, predictors, alpha_ridge[0])

            kolona = int(round(pom_y[len(nizPoteza)]))

            while not da_li_je_popunjena_kolona(tabla,kolona):
                kolona = random.choice([0, 1, 2, 3, 4, 5])
                # kolona = kolona +1
                # if kolona == 6:
                #     kolona = 0


        if da_li_je_popunjena_kolona(tabla,kolona):
            red = get_sledeci_slobodan_red(tabla,kolona)
            postavi_token(tabla,red,kolona,AI_TOKEN)
            fizika(red,kolona,CRNA)
            # Promenljive koje su nam potrebne za cuvanje u traningSetu
            brojPoteza=0
            brojKolone=0
            # Appendovanje novog elemnta, tj kolone koja je odigrana  
            nizPoteza.append(kolona) 
            for i in range(len(nizPoteza)):
                # print("Broj poteza" ,i+1, " AI je odigrao na kolonu ", nizPoteza[i] )
                brojPoteza=i
                brojKolone=nizPoteza[i]

            # Prikupljanje podataka prilikom treniranja igre.
            with open('trainingSet.csv', 'a', newline='') as csvfile:
                imenaPolja = ['brojPoteza', 'brojKolone']
                writer = csv.DictWriter(csvfile, fieldnames=imenaPolja, delimiter='\t')
                writer.writerow({'brojPoteza': brojPoteza+1, 'brojKolone': brojKolone})

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

        # Ako zelimo da resetujemo nas trainingSet, zakomentarisemo deo gde se podaci pune
        # i otkomentarisemo ovo kako bi napravili prazan fajl ( odnosno resetovali traningSet)
        # NIJE PREPORUCLJIBO OVO RADITI !!!

        # with open('trainingSet.csv', 'w', newline='') as csvfile:
        #    imenaPolja = ['brojPoteza', 'brojKolone']
        #    writer = csv.DictWriter(csvfile, fieldnames=imenaPolja, delimiter='\t')

        #    writer.writeheader()


        
            