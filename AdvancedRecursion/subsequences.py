

 
 #tc = o(2 to the power n)
 #sc = o(n)


nums = [6,7,8]

result= []
def sub_sequence(nums,ind,subset):
  if ind >= len(nums):
    result.append(subset.copy())
    return 
  subset.append(nums[ind])
  sub_sequence(nums,ind+1,subset)
  subset.pop()
  sub_sequence(nums,ind+1,subset)
  
  
print(result)
sub_sequence(nums,0,[])
print(result)  