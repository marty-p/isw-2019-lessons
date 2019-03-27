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









# esercizio: creare un file, metterci quello che vogliamo con \n
# l'obbiettivo è quello di leggere il file creato e creare una lista di liste, dove ogni sotto lista contiene una linea del file

# v1
c1=["aaaaaaa\n", "bbbbbbb\n", "ccccccc\n", "ddddddd\n"]
with open("esercizio4file.txt", "w") as f1:
    f1.writelines(c1)
with open("esercizio4file.txt") as f1:
    c2=f1.readlines()
    print(c2)
# v2
c1=["aaaaaaa\n", "bbbbbbb\n", "ccccccc\n", "ddddddd\n"]
c2=[]
with open("esercizio4file.txt", "w") as f1:
    f1.writelines(c1)
with open("esercizio4file.txt") as f1:
    for line in f1.readlines():
        l=[]
        l.append(line)
        c2.append(l)
print(c2)

# v3
c1=["aaaaaaa\n", "bbbbbbb\n", "ccccccc\n", "ddddddd\n"]
c2=[]
with open("esercizio4file.txt", "w") as f1:
    f1.writelines(c1)
with open("esercizio4file.txt") as f1:
    c2 = [line for line in f1.readlines()]
print(c2)

# v4
c1=["aaaaaaa\n", "bbbbbbb\n", "ccccccc\n", "ddddddd\n"]
c2=[]
with open("esercizio4file.txt", "w") as f1:
    f1.writelines(c1)
with open("esercizio4file.txt") as f1:
    c2 = [[line] for line in f1.readlines()]
print(c2)

# v5
c1=["aaaaaaa\n", "bbbbbbb\n", "ccccccc\n", "ddddddd\n"]
c2=[]
with open("esercizio4file.txt", "w+") as f1:
    f1.writelines(c1)
    f1.seek(0)
    c2 = [[line] for line in f1.readlines()]
print(c2)
