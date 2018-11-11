import sys
from threading import Thread, RLock
import time
import random

class Producteur(Thread):
    
    def __init__(self,l,fen,repos):
        Thread.__init__(self)
        self.l = l
        self.fen = fen
        self.repos = repos

    def run(self):
        
        while 1:
            r = random.randint(0, 100)
            String = "(Producteur) Ajout de la valeur : "+str(r)+" - Taille : "+str(self.l.taille())
            self.fen.updateListe(self.l.toString())
            self.fen.updateProd(String)
            self.l.addListe(r)
            time.sleep(self.repos)
            
        
