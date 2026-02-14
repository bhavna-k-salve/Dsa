
#tc =o(m*n)
#sc =o(1)


s ="abcde"
goal = "deabc"

 
# def rotate_str(s,goal):
#   if len(s) != len(goal):
#     return False
#   l = len(s)
#   s= list(s)
#   for _ in range(l):
#     temp = s[l-1]
#     for i in range(l-1,-1,-1):
#       s[i] = s[i-1]
#     s[0] = temp
#     if "".join(s) == goal:
#       return True
#   return False







#tc = o(n+n) similar to o(n)
#sc = o(n+n) similar to o(n)


def rotate_str(s,goal):
  if len(s) != len(goal):
    return False
  cur_str = s+s
  if goal in cur_str:
    return True
  return False

print(rotate_str(s,goal))    