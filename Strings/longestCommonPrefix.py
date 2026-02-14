
#tc=o(m*n)
#sc=o(1)

strs = ["flower","flow","fight"]



def longest_common_factor(strs):
  if len(strs)==0:
    return " "
  result = ""
  base = strs[0]
  for i in range(0,len(base)):
    for word in strs[1:]: 
      if i==len(word) or word[i]!= base[i]:
        return result 
    result += base[i]
  return result

print(longest_common_factor(strs))    
      