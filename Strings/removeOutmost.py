
#tc = o(n)
#sc =o(1)


s = "(()())(())"



def remove_outmost(s):
  count = 0
  result =""
  for ch in s:
    if ch == '(':
      count +=1
      if count > 1:
        result += ch     
    else:
      count -=1
      if count >0:
        result += ch
      
  return   result    
      

print(remove_outmost(s))
    
    