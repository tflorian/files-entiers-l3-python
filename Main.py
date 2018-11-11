from Files import Producteur
from Files import Liste
from Files import Consommateur
from tkinter import *
import Fenetre

#Création des objets liste et fenêtre
l = Liste.Liste()
fen = Fenetre.Fenetre()

#Création du Thread Producteur avec la liste l 
thP = Producteur.Producteur(l,fen,0.1)
thP.daemon = True
thP.start()

#Création des Threads Consommateurs (Demons pour arrêter execution aprés fermeture fenêtre)
thC1 = Consommateur.Consommateur(l,fen,1)
thC2 = Consommateur.Consommateur(l,fen,1)
thC3 = Consommateur.Consommateur(l,fen,1)
thC1.daemon = True
thC2.daemon = True
thC3.daemon = True
thC1.start()
thC2.start()
thC3.start()



fen.fenetre.mainloop()
