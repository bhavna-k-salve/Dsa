
#tc =o(1)
#sc =0(1)


def is_power(num):
  if (num & (num-1)) == 0:
    return "power of 2"
  return "power is not 2"



print(is_power(8))