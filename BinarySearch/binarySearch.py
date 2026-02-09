 
 
 
nums = [2,4,6,7,9,11,18,19]


# def binarySearch(nums,target):
#   l = len(nums)
#   low = 0
#   high = l-1                                               #tc = log2(n)
#   while low <= high:                                        #sc = o(1)
#     mid = (high+low)//2
#     if nums[mid] == target:
#       return mid
#     elif nums[mid] > target:
#       high = mid-1
#     else:
#       low = mid+1
#   return -1    

# print(binarySearch(nums,19))
        
        
        
        

def binarySearch(nums,target,low,high):
  if low > high:
    return -1
  mid = (high+low)//2                                #tc = o(log n )
  if nums[mid] == target:                            #sc = o(log n)
    return mid
  elif nums[mid] > target:
    return binarySearch(nums,target,low,mid-1)
  else:
    return binarySearch(nums,target,mid+1,high)
  

      
     
     

l = len(nums)
print(binarySearch(nums,19,0,l-1))
              