#!python

problem =3D """
The sum of the primes below 10 is 2 + 3 + 5 + 7 =3D 17.

Find the sum of all the primes below two million.

https://projecteuler.net/problem=3D10

"""

print(problem)

top =3D 2000000
primeset =3D [2,3]

possibles=3D[]


x=3D3
while x < top:
  possibles.append(x)
  x+=3D2

p=3D3
while (len(possibles)) > 0:
  zoop1=3Dlen(possibles)
  zoop2=3Dlen(primeset)
  print("current prime:",p,",possibles:",zoop1,",  primeset:",zoop2)
  for x in possibles:
    if ( x % p ) =3D=3D 0:
      possibles.remove(x)
  p=3Dpossibles[0]
  primeset.append(p)
  del possibles[0]
  if p > top**(1/2):
    break

allprimes=3Dprimeset+possibles

sum=3D0
n=3D1
for p in allprimes:
  sum+=3Dp
  print(n,p,sum)
  n+=3D1

