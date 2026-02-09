


# nums = [1,2,3,3,3,3,3,5,6,8,9,9,10]




# def first_last_occ(nums,target):
#   l =len(nums)
#   first =0
#   last =0
#   while nums[first]!=target:                   #tc =o(n)
#     first +=1                                  #sc = o(1)
#   last =first  
#   while nums[last]==target:
#     last+=1
#   return (first,last-1)      
    



nums = [1,2,2,2,2,3,3,3,3,3,3,6,8,9,9,10]

# def first_last_occ(nums,target):
#   l =len(nums)
#   low = 0
#   high = l-1
#   while low <= high:
#     mid = (low+high)//2
#     if nums[mid]==target:
#       low = mid
#       high = mid
#       while nums[low] == target:
#         low -= 1
#       while nums[high] == target:
#         high += 1  
#       return(low+1,high-1) 
#     if nums[mid] >= target:
#       high =mid-1
#     else:
#       low = mid+1   
  
  




# def first_last_occ(nums,target):
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
#   return  (first,last)    
    
    
# print(first_last_occ(nums,3))        








  
  
  


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
  first = lower_bound(nums,target)
  last = upper_bound(nums,target)
  return (first,last)


print(first_last_occ(nums,3))      
      
    






