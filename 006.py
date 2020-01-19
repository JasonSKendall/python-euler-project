#!python

problem = """
The sum of the squares of the first ten natural numbers is,
12 + 22 + ... + 102 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""


#  loop bad.  use math
# https://brilliant.org/wiki/sum-of-n-n2-or-n3/


print(problem)

n=1000000


sumofnumberssquared = ((n+1)*n/2)**2
sumofsquarednumbers = n*(n+1)*(2*n+1)/6
print (int(sumofnumberssquared - sumofsquarednumbers))



short =  ((n+1)*n/2) - ( (2*n+1)/3 )
short *= ((n+1)*n/2)
print (int(short))


