# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 09:46:52 2019

@author: Studente
"""

import Enemy

class Troll(Enemy):
    def __init__(self, name):
        super().__init__(lives=5)
        self.name = name
    def show_life(self):
        print("{} has {} lives \n".format(self.name, self.lives))
        while self.lives > 0:
            self.attack()
            print("remaining lives: {}".format(self.lives))
            print("*"*20)
        else:
            print("enemy died")
if __name__=="__main__":
    urg = Troll("Urg")
    urg.show_life()
