#for best and worst case
#tc = o(nlogn)
#sc = o(1)

#for average case
#tc = o(n²)
#sc = o(1)

nums = [4,1,7,6,3,2,8]

def quick_short(nums,low,high):
  if low < high:
    p_ind = partition(nums,low,high)
    quick_short(nums,0,p_ind-1)
    quick_short(nums,p_ind+1,high)
  return nums

def partition(nums,low,high):
  pivot = nums[low]
  i=low
  j=high
  while i < j:
    while nums[i] <= pivot and i<= high-1:
      i += 1
    while nums[j] > pivot and j>= low +1:
      j -= 1
    if i<j:  
      nums[i],nums[j] = nums[j],nums[i]
  nums[low],nums[j] = nums[j],nums[low]
  return j  


print(quick_short(nums,0,len(nums)-1))