# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 09:59:36 2019

@author: Studente
"""

import sys
print(sys.path)
sys.path.insert(0, '.')
print(sys.path)

try:
    import moduloAcaso
except ModuleNotFoundError:
    pass

import builtins
dir(builtins)
