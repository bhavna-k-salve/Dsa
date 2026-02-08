
#tc =o(1)
#sc =0(1)


def setBit(num,i):
  if ((num>>i)&1) == 1:
    return True
  else:
    return False
  
  
print(setBit(13,1))  