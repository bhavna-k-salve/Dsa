

#tc = o(n* 2 to the power n)
#sc = o(2 to the power n)


nums = [1,2,3]

def subsets(nums):
  n = len(nums)
  total_subset = 1<<n
  result = []
  for num in range(0,total_subset):
    list = []
    for i in range(0,n):
      if num & (1 << i) != 0:
        list.append(nums[i])
    result.append(list)
  return result

print(subsets(nums))


      