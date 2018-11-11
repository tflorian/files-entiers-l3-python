import random
import sys
from threading import Thread, RLock, Condition
import time

verrou = RLock()

class Liste():
    def __init__(self):
        self.liste = []
        self.condition = Condition()

    def afficherListe(self):
        print(self.liste)

    def taille(self):
        return len(self.liste)

    def addListe(self,i):
        try:
            self.condition.acquire()
            while(len(self.liste)>=20):
                self.condition.wait()
        finally:
            self.liste.append(i)
            self.condition.notify()
            self.condition.release()

    def delListe(self):
        try:
            self.condition.acquire()
            while(len(self.liste)==0):
                self.condition.wait()
        finally:
            i = self.liste[0]
            del self.liste[0]
            self.condition.notify()
            self.condition.release()
            return i

    def toString(self):
        with verrou:
            string = "File : <"
            for i in self.liste:
                string = string+str(i)+","
            string = string+">"
            return string
                
            
