
#tc = o(n)
#sc =o(d) d for deapth





exp = "()(())((()()))"



def paranthesis(exp):
  max_depth = 0
  curr_depth = 0
  for brac in exp:
    if brac == '(':
      curr_depth += 1
      max_depth = max(max_depth,curr_depth)
    elif brac == ')':
      curr_depth -= 1
  return max_depth
      
      
print(paranthesis(exp))      
    