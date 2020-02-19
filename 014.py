#!python


from timeit import default_timer as timer
start = timer()


problem = """
https://projecteuler.net/problem=14

The following iterative sequence is defined for the set of positive integers:

n -> n/2 (n is even)
n -> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 b40 b20 b10 b5 b16 b8 b4 b2 b1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been prov
ed yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

"""

print(problem)

chainlist=[]
cachedchains={}
keeplen=0
n=2

while n < 1000000:

  i=n
  chainlist=[i]
  wenttoone=True

  while i != 1:
    if i%2:
      i=(3*i)+1
    else:
      i=int(i/2)
    if i in cachedchains:
      cachedchains[n] = len(chainlist) + cachedchains[i]
      i=1
      wenttoone=False
    else:
      chainlist.append(i)

  if wenttoone:
    cachedchains[n] = len(chainlist)

  if cachedchains[n] > keeplen:
    keeplen=cachedchains[n]
    print(n,keeplen)

  n+=1

print()
print('The starting number 837799 produces a sequence of 525, according to the internet.')

end = timer()
print('Runtime in seconds:',end - start)

