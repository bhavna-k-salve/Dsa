

#tc = o((n(n+1)/2)) similar to o(n²)
#sc = o(1)


nums = [5,7,8,4,1,6,9,2]

def selection(nums):
  l = len(nums)
  for i in range(0,l-1):
    min_ind = i
    for j in range(i+1,l):
      if nums[j] < nums[min_ind]:
        min_ind = j
    nums[min_ind],nums[i] = nums[i],nums[min_ind]  
    
  return nums  


result =selection(nums)  
print(result)        
    