
#tc =o(n)
#sc =o(n)



s = "PAPER"
t = "TITLE"


def isomorphic(s,t):
  if len(s) != len(t):
    return False
  map = {}
  for i in range(0,len(s)):
    char_s = s[i]
    char_t = t[i]
    if char_s in map:
      if map[char_s] != char_t:
        return False
    else:
      map[char_s]=char_t 
  return True    




print(isomorphic(s,t))