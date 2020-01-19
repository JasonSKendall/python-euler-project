#!python

problem = """
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

# Solution is to find the maximum number of consecutive prime factors present in any of the numbers.
#  8 has 3 twos, but 16 has 4.  Therefore, the number must be divisible by 16
#   first, factor each number 1 to 20 into its primes, and put them into a "list"
#   then find the unique primes of that list.
#    then count the number of times each prime appears
#     then check if that number is more than the previous high count of that prime, if so, assign it to a "dictionary"
#       at the end go through the dictionary and now take the "key to the value" power: i.e. the prime to its maximum count.



print(problem)

primeset=[]
primedict={}

top=20

for y in range(2,top+1):

#  first find the set of primes for the number
  print ("find the primes of ", y)
  primeset=[]
  x=2
  while x <= y:
    if (y % x) == 0:
      primeset.append(x)
      y=int(y/x)
      x -= 1
    x+=1
  print ("  " ,primeset)

# now find the unique primes for that number.
  unique_list=[]
  for i in primeset:
    if i not in unique_list:
      unique_list.append(i)

# now for each unique prime find the count of it, and if it's a new max, save it as a key-value pair
  for i in unique_list:
    j=primeset.count(i)
    print("   there are",j ,"instances of prime factor" ,i)
    if i in primedict:
      k=primedict.get(i)
      if j > k:
        primedict[i]=j
    else:
      primedict[i]=j

# now multiply out the items I saved
print ("")
print ("Now loop through the dictionary of pairs...")
bigsum=1
for x,y in primedict.items():
  bigsum2 = bigsum * ( x**y )
  print (x,"to the",y,"power times the existing sum",bigsum,"equals",bigsum2 )
  bigsum=bigsum2

print ("")
print ("The smallest positive number that is evenly divisible by all of the numbers from 1 to",top,"is")
print (bigsum)
