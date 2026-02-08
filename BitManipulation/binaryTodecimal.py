
#tc = o(len(n))
#sc = o(1)


def convertToDecimal(num):
  decimal = 0
  power = 0
  ind = len(num)-1
  while ind >= 0:
    x = int(num[ind])*(2**power)
    decimal += x
    ind -= 1
    power += 1
  return decimal  
    
    
print(convertToDecimal("1101"))    
   