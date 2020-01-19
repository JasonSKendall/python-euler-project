#!python

problem = """
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""

print(problem)

top = 600851475143
primeset = []


print(top)
x = 2
while (top%2) == 0:
  primeset.append(2)
  top=int(top/2)
  print (top)



x = 3
while x < top**(1/2):
  if (top % x) == 0:
    primeset.append(x)
    top=int(top/x)
    print (x,top)
    x -= 2
  x+=2


print ("final list")
for x in primeset:
  print (x)


print (top)
