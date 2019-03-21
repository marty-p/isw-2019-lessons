# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 10:26:45 2019

@author: Studente
"""


# metodo che prende una stringa che contiene tante lettere
# selezioni la lettera, e conti le sue occorenze e ritorni (lettera, conto)
def conta_lettere(stringa):
    #uniq = set(stringa)
    uniq = []
    for let in stringa:
        if let not in uniq:
            uniq.append(let)
    res = []
    for let in uniq:
        cnt = 0
        for c in stringa:
            if c == let:
                cnt += 1
        #res.append((let, stringa.count(let)))
        res.append((let, cnt))
    return res

print(conta_lettere("aaabbbccccbbddd"))
