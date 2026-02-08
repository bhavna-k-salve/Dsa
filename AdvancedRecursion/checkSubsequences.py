


#  tc = o(2 to the power n)
#  sc = o(n)



nums = [2,1,3,6,4]


def is_subsequence(nums,ind,total,subset,target):
  if total == target:
    return True
  elif total > target:
    return False
  if ind >= len(nums):
    return False
  subset.append(nums[ind])
  add = total + nums[ind]
  pick = is_subsequence(nums,ind+1,add,subset,target)
  if pick == True:
    return True
  subset.pop()
  add = total
  not_pick = is_subsequence(nums,ind+1,add,subset,target)
  return not_pick


result = is_subsequence(nums,0,0,[],100)
print(result)