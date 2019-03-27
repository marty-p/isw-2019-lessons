# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 09:24:42 2019

@author: Studente
"""

#create writable file
with open("textfile.txt", "w") as f:
    f.write("hello world\n")

# error f is already closed
iterable=["this is a test\n", "to write new lines\n", "new line"]
f.writelines(iterable)

# without the with clause
f=open("textfile.txt", "a")
f.writelines(iterable)
f.close()

# read content as a list
with open("textfile.txt", "r") as f:
    contents = f.readlines()
    print(contents)

# read content as single str
with open("textfile.txt", "r") as f:
    string = f.read()
    print(string)
