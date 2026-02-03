

#tc = o((n(n+1)/2)) similar to o(n²)
#sc = o(1)


nums = [4,5,7,9,2,3,0,1,6]

def insertion_sort(nums):
  l = len(nums)
  for i in range(1,l):
    if nums[i] < nums[i-1]:
      min_val = nums[i]
      j =i-1
      while nums[j] > min_val and j>=0:
        nums[j+1] = nums[j]
        j -= 1
      nums[j+1] = min_val
      
  return nums      

print(insertion_sort(nums))