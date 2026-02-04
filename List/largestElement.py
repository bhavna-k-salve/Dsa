

#tc = o(n)
#sc = o(1)




nums = [55,32,-97,99,3,67]

# def larg(nums):
#   largest = float("-inf")
#   for num in nums:
#     if num > largest :
#        largest = num
#   return largest


def larg(nums):
  largest = nums[0]
  for num in nums:
    largest = max(num,largest)
  return largest


print(larg(nums))     