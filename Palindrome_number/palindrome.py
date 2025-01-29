def palindrome(x):
  y = x
  rev = 0
  if(x<0):
    return False
  while x:   # while(x) == while(x!=0)
    a = x % 10
    rev = rev * 10 + a
    x = x//2
  return rev == y
    
