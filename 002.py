#!python

problem = """
Each new term in the Fibonacci sequence is generated by adding the previous two terms.
By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million,
find the sum of the even-valued terms.
"""

print(problem)

top = 4000000
x = 1
y = 2
sum = 0
evensum = 0


while y < top:
  if (y % 2) == 0:
    evensum += y
    print (y,evensum)
  sum = x + y
  x = y
  y = sum