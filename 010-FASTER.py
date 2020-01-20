#!python

problem = """
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

https://projecteuler.net/problem=10

"""

print(problem)

top = 2000000
topsqrt = top**(1/2)
primeset = [2]

possibles=[]

x=3
while x < top:
  possibles.append(x)
  x+=2


allremovelist=[]
x=3
while x <= topsqrt:
  x=possibles.pop(0)
  print(x)

  primeset.append(x)
  removethis=x
  currentremovelist=[]
  n=2
  while removethis < top:
    removethis=x*n
    currentremovelist.append(removethis)
    n+=1

  l1=possibles
  l2=set(currentremovelist)
  l3=[y for y in l1 if y not in l2]
  possibles=l3

print("")
print("foo")

runsum=0
for p in primeset:
  runsum+=p
  
for p in possibles:
  runsum+=p

print("142913828922 = right")
print(runsum)

