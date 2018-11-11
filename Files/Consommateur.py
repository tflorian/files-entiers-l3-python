import sys
from threading import Thread, RLock
import time

from tkinter import *

class Consommateur(Thread):
    
    def __init__(self,l,fen,repos):
        Thread.__init__(self)
        self.l = l
        self.fen = fen
        self.repos = repos

    def run(self):
        self.affCons=StringVar()
        self.affConsLabel = Label(self.fen.fenetre, textvariable = self.affCons)
        self.affConsLabel.pack()
        while 1:
            i = self.l.delListe()
            String = "(Consommateur) Suppression de :"+str(i)
            self.affCons.set(String)
            time.sleep(self.repos)

            
