#!python

problem = """
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

https://projecteuler.net/problem=10

"""

print(problem)

top = 2000000
primeset = [2,3]

possibles=[]


x=3
while x < top:
  possibles.append(x)
  x+=2

p=3
while (len(possibles)) > 0:
  zoop1=len(possibles)
  zoop2=len(primeset)
  print("current prime:",p,",possibles:",zoop1,",  primeset:",zoop2)
  for x in possibles:
    if ( x % p ) == 0:
      possibles.remove(x)
  p=possibles[0]
  primeset.append(p)
  del possibles[0]
  if p > top**(1/2):
    break

allprimes=primeset+possibles

sum=0
n=1
for p in allprimes:
  sum+=p
  print(n,p,sum)
  n+=1
