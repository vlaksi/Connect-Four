"""
Modul u kome se odvija glavni deo nase igre, odnosno pokretacki deo
iz koga pokrecemo igru.
"""

import sys
import imageio
import pandas as pd
import easygui
import tkinter as tk
from tk_html_widgets import HTMLLabel


# Ubacivanje nasih modula.
from moduli.darray import *
from moduli.regression import *
from moduli.body import *
from moduli.physis import *


if __name__ == "__main__":
	while (1):
	    gameMode = easygui.enterbox("Unesite 1 ili 2 (mod 1 je mod u kom AI igra po MINMAX algoritmu, mod 2 je mod u kom AI igra po predikciji numerike na osnovu istreniranog dataseta  ")
	    if(gameMode == '1' or gameMode == '2'):
	        break

	

	tabla = kreiraj_tablu()
	game_over = False

	# Konfigurisanje GUI-a
	
	iscrtaj_tablu(tabla)
	pygame.display.update()
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