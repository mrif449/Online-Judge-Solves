import sys
from functools import *

a = sys.stdin.readline()
b = sys.stdin.readline()
j = {}
array = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
def f(i, ab = 1):
    for c in i:
        if c not in array:
            continue
        if c not in j:
            j[c] = 0
        j[c] += ab
f(a)
f(b, -1)
result = reduce(lambda a, b: a + abs(j[b]), j.keys(), 0)
print(result)