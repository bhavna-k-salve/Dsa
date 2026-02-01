

num = int(input("Enter a number: "))
# def factors(num):
#   result =[]
#   for i in range(1,num+1):          #tc = o(n)
#     if num % i == 0:                #sc = o(k)
#       # print(i)
#       result.append(i)
#   return list




# def factors(num):
#   result =[]
#   for i in range(1,(num//2)+1):     #tc = o(n/2)
#     if num % i == 0:                 #sc = o(k)
#       result.append(i) 
#   result.append(num)
#   return list



from math import sqrt
def factors(num):
  result = []
  for i in range(1,int(sqrt(num)+1)):          #tc = o(√n) + o(nlogn)
    if num % i ==0:                             #sc = o(k)
      result.append(i)
      remainder = num // i
      if remainder not in result:
        result.append(remainder)
  return sorted(result)

print(factors(num))
    
