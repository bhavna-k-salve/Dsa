



nums  = [1,2,3,3,3,3,3,5,6,8,9,9,10]




# def count_occ(nums,target):
#   l = len(nums)
#   low = 0
#   high = l-1
#   count = 0
#   while low <= high:
#     mid = (low+high)//2
#     if nums[mid]==target:
#       low = mid
#       high = mid
#       while  nums[low] == target:
#         count += 1
#         low -= 1
#       while nums[high] == target:
#         count += 1
#         high += 1  
#       return count-1
#     if nums[mid] >= target:
#       high = mid - 1
#     else:
#       low = mid + 1  
          



nums  = [1,2,3,3,3,3,3,5,6,8,9,9,10]


# def count_occ(nums,target):
#   l = len(nums)
#   first = -1
#   last = 0
#   for i in range(0,l):                       #tc = o(n) and sc = o(1)
#     if nums[i] == target:
#       if first == -1:
#         first = i
#       last = i    
#   if first == -1:
#     return 0    
#   return  (last-first+1)        
          
# print(count_occ(nums,3))          












#tc = o(2logn) similar to o(logn)
#sc = o(1)
 

def lower_bound(nums,target):
  l = len(nums)
  lb =-1
  low = 0
  high = l-1
  last_value = nums[high]
  if last_value < target:
      return -1
  while low <= high:
    mid = (low+high)//2
    if nums[mid] >=target:
      lb = mid
      high = mid-1
    else:
      low = mid +1    
  return lb 

def upper_bound(nums,target):
  l = len(nums)
  low = 0
  high = l-1
  ub = l
  last_value = nums[high]
  if last_value < target:
    return -1
  while low <= high:
    mid = (low+high)//2
    if nums[mid] <= target:
      ub = mid
      low = mid + 1   
    else:
      high = mid -1
  return ub

def first_last_occ(nums,target):
  lb = lower_bound(nums,target)
  if lb==-1:
    return 0
  ub = upper_bound(nums,target)
  return ub-lb+1


print(first_last_occ(nums,9))      
      
    












