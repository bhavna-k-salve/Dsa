#tc = o(log2(n))
#sc = o(log2(n))

def convert2Binary(num):
  result = " "
  while num > 0:
    rem = str(num % 2)
    num = num // 2
    result += rem
  result =result[ : :-1]
  return result

print(convert2Binary(13))  