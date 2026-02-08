


#  tc = o(2 to the power n)
#  sc = o(n)


nums = [2,1,3,6,4]

# result= []
# def sub_sequence(nums,ind,subset,target):
#   if ind >= len(nums):
#     if sum(subset)==target:
#       result.append(subset.copy())
#     return 
#   subset.append(nums[ind])
#   sub_sequence(nums,ind+1,subset,target)
#   subset.pop()
#   sub_sequence(nums,ind+1,subset,target)
  
  
# print(result)
# sub_sequence(nums,0,[],9)
# print(result)  










 #tc = o(2 to the power n)
 #sc = o(n)


result= []
def sub_sequence(nums,ind,total,subset,target):
  if total==target:
    result.append(subset.copy())
    return 
  elif total>target:
    return 
  if ind >= len(nums):
    return
  subset.append(nums[ind])
  add = total + nums[ind]
  sub_sequence(nums,ind+1,add,subset,target)
  e = subset.pop()
  add -= e
  sub_sequence(nums,ind+1,add,subset,target)
  
  
print(result)
sub_sequence(nums,0,0,[],6)
print(result)













