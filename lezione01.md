```python
>>> dir(1)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
>>> (1).__float__
<method-wrapper '__float__' of int object at 0x6BA8D8B0>
>>> (1).__float__()
1.0
>>> (1).__str__()
'1'
>>> abs
<built-in function abs>
>>> print(input())
jej
jej
>>> isinstance
<built-in function isinstance>
>>> isinstance(1, int)
True
>>> a=[1,2,3,4]
>>> enumerate(a)
<enumerate object at 0x014E2850>
>>>
>>> for i in enumerate(a):
...     print(i)
...
(0, 1)
(1, 2)
(2, 3)
(3, 4)
>>> for i,v in enumerate(a): print(i, v)
...
0 1
1 2
2 3
3 4
>>> range(1,5)
range(1, 5)
>>> for i in range(1,5): i
...
1
2
3
4
>>> for i in range(0,10): i
...
0
1
2
3
4
5
6
7
8
9
>>> for i in range(0,10): i+1
...
1
2
3
4
5
6
7
8
9
10
>>> for i in range(0,10,2): i+1
...
1
3
5
7
9
>>> stringa="python"
>>> stringa
'python'
>>> len(stringa)
6
>>> stringa[0]
'p'
>>> stringa[-1]
'n'
>>> stringa[:3]
'pyt'
>>> stringa[1:]
'ython'
>>> a = 'b'
>>> c = 'd'
>>> a+c
'bd'
>>> stringa.capitalize()
'Python'
>>> stringa.count("yt")
1
>>> stringa.capitalize().count("P")
1
>>> "qualcosa.csv".endswith(".csv")
True
>>> stringa.capitalize().index("P")
0
>>> stringa.isalpha()
True
>>> stringa.isdigit()
False
>>> stringa.islower()
True
>>> stringa.upper()
'PYTHON'
>>>
>>> lista=[1,3,3,'ciao']
>>> lista[0]
1
>>> lista[:2]
[1, 3]
>>> lista[-2:]
[3, 'ciao']
>>> lista[-1]
'ciao'
>>> for i in lista: print(i)
...
1
3
3
ciao
>>>
>>> for i in range(0, len(lista)): print(lista[i])
...
1
3
3
ciao
```


le stringhe sono immutabili
le liste sono mutabili

```python
>>> lista2=[[1,2,3],['ciao',4]]
>>> lista2[0][0]
1
>>> lista2[1][2]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>> lista2[1][1]
4
>>> lista3=[10,23,45]
>>> for item in lista3:
...     lista2.append(item)
...
>>> lista2
[[1, 2, 3], ['ciao', 4], 10, 23, 45]
>>> lista3.count(5)
0
>>> lista3.count(10)
1
>>> lista3.count([1,2,3])
0
>>> lista = [1,4,7,12,3]
>>> lista
[[1, 2, 3], ['ciao', 4], 10, 23]
>>> lista.pop()
23
>>> lista
[[1, 2, 3], ['ciao', 4], 10]
>>> lista.sort()
>>> lista
[1, 3, 4, 7, 12]
>>> lista.sort(reverse=True)
>>> lista
[12, 7, 4, 3, 1]
>>> lista.reverse()
>>> lista
[1, 3, 4, 7, 12]
>>> lista.clear()
>>> lista
[]
>>> lista=[1, 3, 4, 7, 12]
>>> min(lista)
1
>>> max(lista)
12
>>> len(lista)
5
>>> sum(lista)
27
>>> for i,v in enumerate(lista):
...     print(i,v)
...
0 1
1 3
2 4
3 7
4 12
>>> lista=[]
>>> lista2=[1, 3, 4, 7, 12]
>>> lista+=lista2
>>> lista
[1, 3, 4, 7, 12]
>>> lista4 = [i for i in lista]
>>> lista4
[1, 3, 4, 7, 12]
>>> lista5 = lista.copy()
>>> lista5
[1, 3, 4, 7, 12]
>>> lista6 = [i for i in lista if i >5]
>>> lista6
[7, 12]
```
