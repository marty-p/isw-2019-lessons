# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

### strings are immutable
a="""  asd  """
print("(%s)" % a.strip())


a="a,b,c,d"
print(a.split(","))
for e in a.split(","):
    print(e)

# get user input and split it by space
a=input()
for e in a.split():
    e = e.strip()
    print(e)

# take a list of ints (as strings) and make a sum of it
a=["12", "5454", "854"]
b=[int(e.strip()) for e in a]
print(b, sum(b))
#alt ways
print(sum(map(int, a)))

### lists are mutable and ordered
#by copy
a=[1,2]
b=list(a)
c=a.copy()
a[0]=3
print(a,b,c)

### range
#range
a=[]
for i in range(0, 10):
    a.append(i)

#list comprension
b=[i for i in range(0, 10)]
print(a,b)

#make a list of different items between the two lists
d = [[i,j] for i in [1,2,3] for j in [3,4,5] if i != j]
print(d)

#nested list comprensions (inverts rows with columns)
matrix = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
new_matrix = [[row[i] for row in matrix] for i in range(4)]
print(new_matrix)


### tuples are immutable but ordered
a=(1,2,3,4)
b=tuple([1,2,3,4])
c=tuple("1234")
print(a,b,c)

#tuples' children can't be edited
a[1]=5 # TypeError

#but lists inside tuples are mutable (sub-children)
a=([1,2,3,4])
a[0][1]=5 # OK

# tuple packing
a=1,2,3,4
print(a)

### sets (insiemi) unique, mutable and unordered
a={1,2,3,3,3,3,5,6,7}
print(a)

#add single element
a.add(8)
a.add(8)
a.add(8)
print(a)

#add an array of elements
a.update({8,8,8,8,9,9,9,9})
print(a)

#remove element 2 (not index 2)
a.remove(2)
print(a)

#clear set
a.clear()
print(a)

# set operations
a=set('abracadabra')
b=set('alacazam')
print(a,b)

# a characters included in b (difference)
c=a-b
print(c, a.difference(b))

# merged characters (union)
c=a|b
print(c, a.union(b))

# intersected characters (inersected)
c=a&b
print(c, a.intersection(b))

# set comprensions
c = {i for i in a if i not in b} #difference
print(c)

### dictionaries / dicts (dizionari) unordered, mutable and unique keys, couples of (keys, values)
a={"a":1, "b":2, "c":3}
print(a)
print(a["a"])
a["d"]=4
a.update({"e":5, "f":6})
print(a)

#create from lists of (key, value)
a=dict([('aaa',111),('bbb',222)])
print(a)

#iterate only the keys
for k in a.keys(): print(k)

#iterate only the values
for v in a.values(): print(v)

#iterate the items
for i in a.items(): print(i)

#delete an item returning it
a.pop('bbb')
print(a)
#or (but ugly)
del a['aaa']
print(a)

#dict comprension
scores=[12,81,64,18]
names=['guido', 'jacob', 'jack', 'james']
res={j:scores[i] for i,j in enumerate(names)}
print(res)








