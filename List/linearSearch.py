


nums = [5,3,9,8,1,6,4,-10,-100]

def linear_search(target):
  for i in range(0,len(nums)):                         #tc=o(n)
    if nums[i] == target:                               #sc=o(1)
      return i
  return -1  

print(linear_search(1))    