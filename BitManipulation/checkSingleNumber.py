
#tc =o(n)
#sc =0(1)

nums = [5,1,3,3,7,1,7]


def checkNumber(nums):
  ans = 0
  for num in nums:
    ans = ans ^ num
  return ans  



print(checkNumber(nums))