
#tc = o(2nlogn) similar to o(nlogn)
#sc = o(2n) similar to o(n)

s = "anagram"
t = "nagaram"



# def valid_Anagram(s,t):
#   if len(s) != len(t):
#     return False
#   sort_s = sorted(s)
#   sort_t = sorted(t)
#   if sort_s == sort_t:
#     return True
#   return False










#tc = o(n)+o(n) similar to o(n)

def valid_Anagram(s,t):
  if len(s) != len(t):
    return False
  chars_freq = {}
  for ch in s:
    chars_freq[ch] = chars_freq.get(ch,0)+1
  for ch in t:
    if ch not in chars_freq:
      return False
    else:
      if chars_freq[ch] == 0:
        return False
      else:
        chars_freq[ch] -= 1
  return True
        


print(valid_Anagram(s,t))