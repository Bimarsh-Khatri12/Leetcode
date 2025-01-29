#Recursion
def myPow(x,n):
  if n == 0:
    return 1
  elif (n<0):
    return myPow(1/x,abs(n))
  elif (n%2==0):
    return myPow(x*x, n/2)
  else:
    return x * myPow(x, n-1)

#Binary Exponentation
def myPow(x,n):
  if(n<0):
    x = 1/x
    n = abs(n)
    res = 1
  while(n): # It is equivalent to while(n!=0)
    if(n & 1): #It is equivalent to n%2==1
      res = res * x
    x = x * x
    n>>=1 # It is equivalent to n = n/2
  return res
  
