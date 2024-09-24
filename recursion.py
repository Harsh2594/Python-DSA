#Build a recusive function to print first n natural number
def printN(n):
  if n>0:
    printN(n-1)
    print(n,end=" ")

printN(10)
print()    

#Build a recusive function to print first n natural number in reverse order

def printReverseN(n):
  if n == 1:
    print(n)
  else:
    print(n,end=" ")
    printReverseN(n-1)

printReverseN(10)

#print sum of first N natural number:

def sum(n):
  if n == 1:
    return 1
  else:
    s = n + sum(n-1)
  return s

print(sum(10))
  
#print sum of first N odd natural number:  

def sumodd(n):
  if n == 1:
    return 1
  else:
    sumOdd = (2*n-1) + sumodd(n-1)
  return sumOdd  

print(sumodd(3))

#print sum of first N even natural number:

def sumEven(n):
  if n == 1:
    return 2
  else:
    sumeven = (2*n) + sumEven(n-1)
  return sumeven  

print(sumEven(3))

#Calculate factorial of a number:

def factorial(n):
  if n == 1:
    return 1
  else:
    fact = n * factorial(n-1)
  return fact

print(factorial(3))
  
#calculate sum of square of first natural number:

def squareN(n):
  if n == 1:
    return 1
  else:
    squa = n**2 + squareN(n-1)
  return squa

print(squareN(3))    

#print odd natural number in reverse order:

def oddReverse(n):
  if n == 1:
    print(n)
  else:
    print(2*n-1,end=" ")
    oddReverse(n-1)

oddReverse(5)

