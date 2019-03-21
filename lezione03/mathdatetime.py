# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 10:20:10 2019

@author: Studente
"""

import math
math.cos(math.pi/4)

math.sqrt(81)


import random
random.choice(["apple","pear","banana","watermelon"])

random_numbers = random.sample(range(100), 10)
print(random_numbers)

random.random()


import statistics
data = [1.45, 2.34, 1.67, 3]

avg = statistics.mean(data)
round(avg, 2)

statistics.median(data)
statistics.variance(data)


from datetime import date
today=date.today()
print(today)

birthday=date(1984, 6, 13)
print(birthday)

age = today - birthday
print(age)
