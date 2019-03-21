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

# metodo che prende una stringa che contiene tante lettere
# selezioni la lettera, e conti le sue occorenze e ritorni (lettera, conto)
def conta_lettere_input():
    print("inserisci una lista di stringhe:")
    stringhe = input()
    for stringa in stringhe.split():
        print(conta_lettere(stringa))

conta_lettere_input()


# metodo che prende una stringa che contiene tante lettere
# selezioni la lettera, e conti le sue occorenze e ritorni (lettera, conto)
def conta_lettere_input_2():
    print("inserisci una lista di stringhe:")
    stringhe = input()
    stringa = ""
    for let in stringhe:
        if let == " ":
            print(conta_lettere(stringa))
            stringa = ""
        else:
            stringa += let
    if stringa:
        print(conta_lettere(stringa))

conta_lettere_input_2()



# metodo che prende una stringa che contiene tante lettere
# selezioni la lettera, e conti le sue occorenze e ritorni (lettera, conto)
def conta_lettere_input_3():
    print("inserisci una lista di stringhe:")
    stringhe = input()
    stringhe.strip()
    while len(stringhe):
        s = stringhe.find(" ")
        if (s==-1):
            print(conta_lettere(stringhe))
            break
        else:
            print(conta_lettere(stringhe[:s-1]))
            stringhe = stringhe[s+1:]

conta_lettere_input_3()




