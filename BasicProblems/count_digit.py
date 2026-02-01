

# num = int(input("Enter a number : "))
# def count_digit(num):
#   n = num
#   count=0                   #tc= o(log10(n))
#   while n > 0:              #sc = o(1)
#     count += 1
#     n = n//10  
#   return count
# print(count_digit(num))


import math
num = int(input("Enter a number : "))
def count_digit(num):
  return int(math.log10(num)+1)
print(count_digit(num))