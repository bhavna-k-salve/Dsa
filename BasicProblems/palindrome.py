

#tc = o(log10(n))
#sc = o(1)



num = eval(input("enter a value:"))

def palindrome(num):
  n = num
  reverse = 0
  while n > 0:
    remainder = n % 10
    reverse = (reverse * 10)+remainder
    n = n//10
    
  # if reverse == num:
  #   return "palindrome"
  # else:
  #   return "Not palindrome"    
  return reverse == num
    
print(palindrome(num))   