

#tc = o(n)
#sc = o(1)


num ="MCMXCIV"

def roman_to_integer(num):
  letter = {
    'I':1,
    'V':5,
    'X':10,
    'L':50,
    'C':100,
    'D':500,
    'M':1000
  }
  n = len(num)
  result = 0
  for i in range(0,n):
    if i<n-1 and letter[num[i]]<letter[num[i+1]]:
      result -= letter[num[i]]
    else:
      result+= letter[num[i]]  
  return result    
      
      
print(roman_to_integer(num))      