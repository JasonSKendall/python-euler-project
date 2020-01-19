#!python

problem = """
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

##

print(problem)


x = 10000
y = 10000
maxx = 0

while x < 99999:
  while y < 100000:
    producz = x*y
    chkproductz=str(producz)
    first=chkproductz[0]
    laast=chkproductz[-1]
    if first == laast:
      reversit=chkproductz[::-1]
      if reversit == chkproductz :
        if producz > maxx:
          maxx = producz
          print (x,y,maxx)
    y+=1
  x+=1
  y=x
