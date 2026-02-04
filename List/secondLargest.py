

nums = [55,32,97,-55,45,32,88,21,97]



# def second_largest(nums):
#   largest = nums[0]
#   for num in nums:                   #tc = o(n)
#     if num > largest:                 #sc = o(1)
#       largest = num  
#   return nums[-2]






# def second_largest(nums):
#   largest = float("-inf")
#   sec_larg = largest
#   for num in nums:                   #tc =o((2n) similar to o(n)
#     if num > largest:                 #sc = o(1 )
#       largest = num
#   for num in nums:
#     if  num != largest and num > sec_larg:
#        sec_larg = num          
#   return sec_larg    







def second_largest(nums):
  largest = float("-inf")
  sec_larg = largest
  for num in nums:                                 #tc = o(n)
    if num > largest:                              #sc = o(1 )
      sec_larg = largest            
      largest = num
    if  num < largest and num > sec_larg:
       sec_larg = num   
        
  return sec_larg

print(second_largest(nums))