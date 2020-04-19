#! /usr/bin/python3
import sys
from math import *

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

p = ((a + b + c)/2)
print(p)
if a + b > c and a + c > b and b + c > a:
    print("Треугольник существует")
    s = sqrt(p*(p-a)*(p-b)*(p-c))
    print(s)
else:
    print("Треугольник не существует")
