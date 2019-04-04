# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 09:44:56 2019

@author: Studente
"""

import random
class Enemy:
    def __init__(self, lives):
        self.lives = lives
    def attack(self):
        if random.randint(0,1)==0:
            print('enemy not heated')
        else:
            self.lives -= 1
            print('enemy heated')