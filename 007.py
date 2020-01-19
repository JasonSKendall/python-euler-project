#!python

problem = """
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?
"""

#  loop bad.  use math
# https://projecteuler.net/problem=7


print(problem)

import math

top=10001
primeset=[2,3]
m=1
x=len(primeset)


def check_prime(n):
  global x,primeset
  primetest=True
  topn=math.sqrt(n)
  for i in primeset:
    if i > topn:
      break
    if (n%i) == 0:
      primetest=False
  if primetest == True:
    primeset.append(n)
    x=len(primeset)
    print("found",x,n)

while x < top:
  check_prime((6*m)-1)
  check_prime((6*m)+1)
  m+=1

#print (primeset)

