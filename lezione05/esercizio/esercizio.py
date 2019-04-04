# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 10:03:31 2019

@author: Studente
"""

# creare una classe a cui verrà passata una lista di stringhe.
# creare un metodo che verifichi quante parole nella lista hanno lettere doppie
# quante hanno lettere ripetute.
# Esempio: 'doppia' ha una doppia mentre 'casa' ha la 'a' ripetuta, invece 'cassa'
# ha sia doppia che ripetute e va contata per ambo i casi

class Conta:
    def __init__(self, lista):
        self.lista = lista
    def __conta_ripetute(self, word):
        mappa={}
        for c in word:
            try:
                mappa[c] += 1
            except KeyError:
                mappa[c] = 1
        for k,v in mappa.items():
            if v > 1:
                print("il carattere {} è ripetuto {} volte".format(k,v))

    def __conta_doppie(self, word):
        prev = ''
        doppie=set()
        for c in word:
            if prev and c==prev:
                doppie.add(c)
            prev = c
        for v in doppie:
            print("il carattere {} è doppio".format(v))

    def conta(self):
        for s in self.lista:
            print("processando... {}".format(s))
            self.__conta_doppie(s)
            self.__conta_ripetute(s)
        pass

if __name__=='__main__':
    conta = Conta(["casa", "cassa", "doppia", "lello"])
    conta.conta()
