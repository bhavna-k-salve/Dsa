


# nums = [2,3,4,7,5,9,1,6]

# def BUbble_sort(nums):
#   l = len(nums)
#   for j in range(0,l):                       #tc = o(n²)
#     for i in range(0,l-1):                    #sc = o(1)
#       if nums[i] > nums[i+1]:
#         nums[i],nums[i+1] = nums[i+1],nums[i]
#   return nums 




# def BUbble_sort(nums):
#   l = len(nums)
#   for j in range(l-2,-1,-1):                      #tc = o((n(n+1))/2) similar to o(n²)
#     for i in range(0,j+1):                         #sc = o(1)
#       if nums[i] > nums[i+1]:
#         nums[i],nums[i+1] = nums[i+1],nums[i]
#   return nums 
 
 
 
 
 
 #For best case

nums = [1,2,3,4,5,6,7,9,8,9]

def BUbble_sort(nums):
  l = len(nums)
  is_swap = False
  for j in range(l-2,-1,-1):                      #tc = o((n(n+1))/2) similar to o(n²)
    for i in range(0,j+1):                         #sc = o(1)
      if nums[i] > nums[i+1]:
        nums[i],nums[i+1] = nums[i+1],nums[i]
        is_swap = True
    if is_swap == False:
      break     
  return nums  


print(BUbble_sort(nums))    