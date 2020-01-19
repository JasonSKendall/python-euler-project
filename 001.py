#!python

print("hello world")

#
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
#

top = 999
x = 3
y = 5
z = 15



sum = 0
topx = int(top/x)
topy = int(top/y)
topz = int(top/z)
sumx = x * ( topx + 1 ) * topx
sumy = y * ( topy + 1 ) * topy
sumz = z * ( topz + 1 ) * topz
sum = int(( sumx + sumy - sumz ) /2 )
print (sum)




sum = 0
i = 1
while i <= top:
  k = i % x
  j = i % y
  if j == 0 or k == 0 :
    sum += i
  i += 1
