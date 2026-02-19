
#tc = o(n)
#sc = o(n)


def valid_paranthesis(str):
  stack = []
  if len(str)==0:
    return False
  for i in range(0,len(str)):
    if str[i] == '[' or str[i] == '(' or str[i] == '{':
      stack.append(str[i])
    else:
      stack.pop()
  return len(stack) == 0
       



str = "{[({[()]})]}"
print(valid_paranthesis(str))