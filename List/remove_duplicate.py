nums = [1,1,1,2,3,4,4,7,9,9,9,10]

# print(list(set(nums)))




# def remove_duplicates(nums):
#   freq_map = {}
#   for i in nums:                #tc = o(2n) similar to o(n)
#     freq_map[i] =0              #sc = o(n)
#   j = 0
#   for i in freq_map:
#     nums[j] = i
#     j += 1
#   return nums 








def remove_duplicates(nums):
  i = 0
  j = 1
  if len(nums) <= 1:
    return nums[0]
  while j < len(nums):                                #tc = o(n)
    if nums[j] > nums[i]:                              #sc = o(1)
      nums[i+1],nums[j] =nums[j],nums[i+1]
      i += 1
    j+=1  
   
  return nums 
    
  
  
  
print(remove_duplicates(nums)) 
    
    