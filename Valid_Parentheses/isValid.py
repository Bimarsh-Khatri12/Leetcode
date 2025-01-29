# Iteration approach
def isValid(s):
  stack = []
  for c in s:
    if(c == '(' or c == '[' or c == '{'):
      stack.append(c)
    else:
      if not stack:
        return False
      if c == ')' and stack[-1] != '(':
        return False
      if c == '}' and stack[-1] != '{':
        return False
      if c ==']' and stack[-1] != '[':
        return False
      stack.pop()
  return not stack

#Hashmap
def isValid(s):
  dict = {'(':')','{':'}','[':']'}
  stack = []
  for c in s:
    if c in dict:
      stack.append(c)
    elif not stack or d[stack.pop()] != c:
      return False
  return not stack
