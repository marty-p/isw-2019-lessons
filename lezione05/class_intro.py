# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 09:18:06 2019

@author: Studente
"""

class Foo(object):
    i=1
    def printer(self, string):
        print(string)

foo_instance = Foo()

print(foo_instance.i)

foo_instance.i = 10
print(foo_instance.i)

foo_instance.printer('ciao')

class Superheroes():
    kind = 'superheroes'
    def __init__(self, hero):
        self.hero = hero

inst_1 = Superheroes('Superman')
inst_2 = Superheroes('Batman')
inst_3 = Superheroes('Spiderman')

print(inst_1.kind)
print(inst_2.kind)
print(inst_3.kind)

print(inst_1.hero)
print(inst_2.hero)
print(inst_3.hero)
