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


