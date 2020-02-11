"""
Modul u kome se nalazi simulacija fizike u nasoj igri.
"""

from threading import Thread, Event
import time
from .constant import *

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
