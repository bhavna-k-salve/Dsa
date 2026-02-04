nums = [1,0,2,4,3,0,0,3,5,1]

# def moveZeros(nums):
#   hash_list =[]
#   count =0
#   for i in nums:                              #tc = o(n)
#     if i != 0:                                 #sc =o(n)
#       hash_list.append(i)
#     if i == 0:
#       count += 1  
     
#   return (hash_list + [0]*count)






def moveZeros(nums):
  i =0
  j=0
  if len(nums) == 1:
    return 
  if i == len(nums):                       #tc = o(n)
    return                                 #sc =o(1)
  j =i+1 
  while j < len(nums):
    if nums[i] ==0:
      break
    i+=1
  while j < len(nums):
    if nums[j] != 0 :
      nums[i],nums[j]=nums[j],nums[i]   
      i+=1  
    j+=1
  return nums  
    

print(moveZeros(nums))

