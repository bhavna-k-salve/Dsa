

#  tc = o(2 to the power n)
#  sc = o(n)


nums = [7,1,6,2,5,3,4]


def check_count(nums,ind,total,target):
  if total == target:
    return 1
  elif total > target:
    return 0
  if ind >= len(nums):
    return 0
  add = total+nums[ind]
  pick = check_count(nums,ind+1,add,target)
  add = total
  not_pick =check_count(nums,ind+1,add,target)  
  return (pick + not_pick)


res = check_count(nums,0,0,7)
print(res)