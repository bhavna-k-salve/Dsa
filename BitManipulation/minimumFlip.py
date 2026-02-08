
#tc =o(32)
#sc =0(1)



def minimumFlip(start,goal):
  ans = start ^ goal
  count = 0
  for i in range(0,32):
    if ans & (1<<i) != 0:
      count += 1
  return count


print(minimumFlip(13,2))    