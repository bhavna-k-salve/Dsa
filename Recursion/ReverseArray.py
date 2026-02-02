
#tc = o(n/2) similar to o(n)
#sc = o(n/2) similar to o(n)

n= [2,3,8,9,5,10,6,4]

def ReverseArray(n,left,right):
  if left >= right :
    return n
  n[left],n[right] = n[right],n[left]
  return ReverseArray(n,left+1,right-1)
  
result = ReverseArray(n,2,5) 
print(result)






# left = 0
# right = 7
# while left <= right:
#   n[left],n[right] = n[right],n[left]
#   left += 1
#   right -= 1
  
# print(n)  
  