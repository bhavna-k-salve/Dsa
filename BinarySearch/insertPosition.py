



#tc = o(log2(n))
#sc = o(1) 


nums = [1,3,4,5,8,9,14,15,19,20,21]
 
 
 

def insert_position(nums,target):
  l = len(nums)
  low = 0
  high = l-1
  lb = -1
  if nums[high] < target:
    return l
  while low <= high:
    mid = (low+high)//2
    if nums[mid] >=target:
      lb = mid
      high =mid-1
    else:
      low =mid +1
  return lb    

print(insert_position(nums,4))