# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 10:14:57 2019

@author: Studente
"""
#https://finance.yahoo.com/quote/BTC-USD/history?period1=1428703200&period2=1554933600&interval=1d&filter=history&frequency=1d

#1. costruisci una classe che prende il percorso del file csv
#2. poi avete un metodo opendataset che apre il file scaricato
#oltre ad aprire il csv deve verificare che ci sia 'Close'
#convertirla in numpy array
#3. poi creare un altro metodo
#che aggiunge in maniera random dei np.nan nel numpy array
#4. mettere i nan e poi toglierli mettendoci la media dei 6 valori sopra


import pandas as pd
import numpy as np
import random

class EsReader:
    
    def __init__(self, filename):
        self.filename = filename
        
    def readData(self):
        # read file
        self.dataset = pd.read_csv(self.filename, sep=',')
        # convert Close to close
        self.dataset.columns = map(str.lower, self.dataset.columns)
        # check if close exists
        if 'close' in self.dataset:
            self.closeSet = self.dataset['close'].values
            return True
        return False
        
    def addRandom(self):
        #randomSet = np.array(random.sample(range(100), 20))
        randomSet = np.array([np.nan]*40)
        self.closeSet = np.append(self.closeSet, randomSet)

    def calcNan(self, r=6):
        for i,v in enumerate(self.closeSet):
            if np.isnan(self.closeSet[i]):
                #print(self.closeSet[i-r:i])
                self.closeSet[i]=np.average(self.closeSet[i-r:i])


if __name__ == '__main__':
    filename = r"C:\Users\Studente\Desktop\isw\lezione06\esercizio\BTC-USD.csv"
    esReader = EsReader(filename)
    esReader.readData()
    #print(esReader.dataset.columns)
    #print(esReader.closeSet)
    esReader.addRandom()
    #print(esReader.closeSet)
    esReader.calcNan()
    a=esReader.closeSet
