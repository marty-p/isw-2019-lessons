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

