# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 10:01:41 2019

@author: Studente
"""

import json

# dump string to json file
with open("jsonfile.json", "w") as f:
    json.dump("hello world", f)

# data struct to json string
x=[(1,2),('ciao',4)]
print(json.dumps(x))

# data struct to json file
x=[(1,2),('ciao',4)]
with open("jsonfile.json", "w") as f:
    json.dump(x, f)

# json file to data struct
with open("jsonfile.json", "r") as f:
    res = json.load(f)
    print(res)

# useful to read config files with dicts
with open("conf.json", "r") as f:
    conf = json.load(f)
