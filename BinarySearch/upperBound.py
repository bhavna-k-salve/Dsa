


#tc = o(log2(n))
#sc = o(1)


nums = [1,1,1,2,3,3,5,6,7,7,7,9,12,12,13]


def upper_bound(nums,target):
  l = len(nums)
  low = 0
  high = l-1
  ub = l
  last_value = nums[high]
  if last_value < target:
    return -1
  while low <= high:
    mid = (low+high)//2
    if nums[mid] <= target:
      ub = mid
      low = mid + 1   
    else:
      high = mid -1
  return ub


print(upper_bound(nums,3))      