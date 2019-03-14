```python
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


a="""  asd  """
print("(%s)" % a.strip())


a="a,b,c,d"
print(a.split(","))
for e in a.split(","):
    print(e)

a=input()
for e in a.split():
    e = e.strip()
    print(e)

a=["12", "5454", "854"]
b=[int(e.strip()) for e in a]
print(b, sum(b))
print(sum(map(int, a)))

### liste
a=[1,2]
b=list(a)
c=a.copy()
a[0]=3
print(a,b,c)

```
