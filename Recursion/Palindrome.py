


m = "nitin"
left =0
right = len(m)-1

# def palindrome(n,left,right):
#   if left >= right:
#     if n[left] != n[right]:
#       return False
#     return True
#   return  palindrome(n,left+1,right-1)

# print(palindrome(m,left,right))





def palindrome(n,left,right):
  while left <= right:
    if n[left] != n[right]:
      return False
    left += 1
    right -= 1
  return True
  
print(palindrome(m,left,right))

  
      
      
    
  

   