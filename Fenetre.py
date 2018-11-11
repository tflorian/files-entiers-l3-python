from tkinter import *
from threading import Thread, RLock


class Fenetre():

    def __init__(self):
        self.fenetre = Tk()
        self.fenetre.geometry("600x200")
        self.affListe=StringVar()
        self.affProd=StringVar()
        self.affListeLabel = Label(self.fenetre, textvariable = self.affListe)
        self.affProdLabel = Label(self.fenetre, textvariable = self.affProd)
        self.affListeLabel.pack()
        self.affProdLabel.pack()

    def updateListe(self,String):
        self.affListe.set(String)

    def updateProd(self,String):
        self.affProd.set(String)
