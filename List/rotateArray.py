


nums = [5,-2,3,9,0,6,10,7]

# def rotate(nums):
#   #print(id(nums))
#   n = int(input("how many times you want to rotate the list:"))     #tc = o(n)
#   l = len(nums)                                                     #sc = o(1)
#   k = n % l
#   nums[:] = nums[l-k:] + nums[:l-k]
#   #print(id(nums))
#   return nums





# def rotate(nums):
#   n = int(input("how many times you want to rotate the list:"))     #tc = o(n)
#   l = len(nums)                                                     #sc = o(1)
#   temp = nums[l-1]
#   for i in range(l-2,-1,-1):
#     nums[i+1] = nums[i]
#   nums[0] = temp  
#   return nums






# def rotate(nums):
#   n = int(input("how many times you want to rotate the list:"))     #tc = o(k*n)
#   l = len(nums)                                                     #sc = o(1)
#   k = n % l
#   count =0
#   while count < k:
#     temp = nums[l-1]
#     for i in range(l-2,-1,-1):
#       nums[i+1] = nums[i]
#     nums[0] = temp  
#     count += 1
#   return nums







def reverse(nums,left,right):
  while left<right:
    nums[left],nums[right] = nums[right],nums[left]
    left += 1
    right -= 1

def rotate(nums):
  n = int(input("how many times you want to rotate the list:"))     #tc = o(n)
  l = len(nums)                                                     #sc = o(1)
  k = n % l
  reverse(nums,l-k,l-1)
  reverse(nums,0,l-k-1)
  reverse(nums,0,l-1)
  return nums
  
  
print(rotate(nums))