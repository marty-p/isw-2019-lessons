# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 10:12:37 2019

@author: Studente
"""

# take a number
while True:
    try:
        x = int(input("please enter a number: "))
        break
    except ValueError:
        print("no valid input")

# take a number and divide
while True:
    try:
        inp = int(input('numero: '))
    except:
        print('solo numero non stringhe')
    try:
        x = 1/inp
        break
    except ZeroDivisionError:
        print('attento, stai dividendo per zero')

# altra soluzione
while True:
    try:
        inp = int(input('numero: '))
        x = 1/inp
        break
    except (ValueError, ZeroDivisionError) as err:
        if isinstance(err, ValueError):
            print('solo numero non stringhe')
        else:
            print('attento, stai dividendo per zero')

# else clause in try except block, useful when try clause doesn't raise an except
while True:
    try:
        x = int(input("please enter a number: "))
    except ValueError:
        print("no valid input")
    else:
        print("nessun errore generato")
        break

# finally always run
while True:
    try:
        x = int(input("please enter a number: "))
        break
    except ValueError:
        print("no valid input")
    else:
        print("finally")

# finally always run
while True:
    try:
        x = int(input("please enter a number: "))
        break
    except:
        raise ValueError("no valid digit")

# esercizio: scrivere un programma che richieda di inserire un punto del piano
# cartesiano, quindi l'utente deve inserire due numeri separati da uno spazio
# o da una virgola. il punto verrà considerato solamente se appartenente al I
# o al III quadrante. i punti già inseriti non devono essere considerati.
# l'utente deve inserire numero non stringhe. il punto deve essere realmente un
# punto del piano cartesiano (controllo sulla lunghezza dell'input inserito)
#
piano_len = (50, 50, -50, -50)

def get_input_point():
    res = (0,0)
    while True:
        i = input("please enter a point: ")
        # skip empty lines
        if not i.strip():
            continue
        # check for empty spaces
        r1=i.split(" ")
        if not len(r1)==2: # must have x y
            r1=i.split(",") # if not split for ,
            if not len(r1)==2: #and recheck
                print("no valid input")
                continue # then repeat
        try:
            res=[int(i) for i in r1]
        except ValueError:
            print("no valid input")

        # check if within plane
        if res[0] > piano_len[0]:
            print("x > region I x")
            continue
        elif res[1] > piano_len[1]:
            print("y > region I y")
            continue
        elif res[0] < piano_len[2]:
            print("x < region III x")
            continue
        elif res[1] < piano_len[3]:
            print("y < region III y")
            continue
        break
    return res
get_input_point()
