
#tc = o(nlog2(n))
#sc = o(n)


nums =[3,2,4,1,5,8,6,4]

def mergeSort(nums):
  
  if len(nums) <=1:
    return nums
  mid =len(nums)//2
  leftarray = nums[ :mid]
  rightarray = nums[mid:]
  leftsort = mergeSort(leftarray)
  rightsort = mergeSort(rightarray)
  return mergeArray(leftsort,rightsort)
  
def mergeArray(leftarray,rightarray):
  result = [] 
  i = 0
  j = 0
  m = len(leftarray)
  n = len(rightarray)
  while i<m and j<n:
    if leftarray[i] <= rightarray[j]:
      result.append(leftarray[i])
      i += 1
    else:   
      result.append(rightarray[j])
      j += 1
  if i < m:
    while i < m:
      result.append(leftarray[i])
      i += 1
  if j < n:
    while j <n:
      result.append(rightarray[j])  
      j += 1
        
  return result

print(mergeSort(nums))       
  
  