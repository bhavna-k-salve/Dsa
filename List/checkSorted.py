


nums = [3,5,6,8,0,9,10,20]


def is_Sorted(nums):
  for i in range(0,len(nums)-1):          #tc = o(n)
    if nums[i] > nums[i+1]:                 #sc = o(1)
      return False    
  return True

  
print(is_Sorted(nums))  
  