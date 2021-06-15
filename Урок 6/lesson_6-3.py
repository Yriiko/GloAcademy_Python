# Задание 3
from math import *
a = input()
b = input()
c = input()

d = len(a)
e = len(b)
f = len(c)

g = max(d, e, f)

if g == d:
    print(a)
elif g == e:
    print(b)
else:
    print(c)
