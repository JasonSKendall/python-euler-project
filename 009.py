#!python

problem = """
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

# https://projecteuler.net/problem=9


print(problem)

import math


a=1
b=2
z=999
while b<497:
  while a<b:
    z=a**2 + b**2 - ( 1000-a-b )**2
    if z==0:
      aa=a
      bb=b
    print(a,b,z)
    a+=1
  a=1
  b+=1


c=1000-aa-bb
print("")
print(aa/25,bb/25,c/25)
print(aa,bb,c)
print(aa**2,bb**2,c**2)
print(aa*bb*c)
