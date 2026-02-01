


#tc = o(log10(n))
#sc = o(1)


num = int(input("Enter a number:"))

def armstrong(num):
  n = num
  m = num
  count=0
  # while n > 0:
  #   count += 1
  #   n = n//10
  count = len(str(n))
  
  result =0  
  while m > 0:
    remainder = m % 10
    result = (remainder ** count) +result
    m = m // 10
    
  # if reverse == num:
  #   return "Armstrong"
  # else:
  #   return "Not armstrong"   
  return num == result  


print(armstrong(num))
    
    
      
  