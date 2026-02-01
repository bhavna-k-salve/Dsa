n=[5,3,2,2,1,5,5,7,5,10]
m=[10,111,1,9,5,67,2]


# def count_frequency(n,m):
#   for num1 in m:
#     count = 0                                   #tc = o(m*n)
#     for num2 in n:                              #sc = o(1)
#       if num1 == num2:
#         count += 1
#     print(num1 ,"-->" ,count)  
    
    


# def count_frequency(n,m):
#   hash_list = [0]*11
#   for num in n:
#     hash_list[num] += 1                 #tc = o(m+n)                                           
#   for  num in m:                          #sc = o(11) similar to o(1)
#     if num<1 or num>10:
#       print("0")
#     else:
#       print(hash_list[num])   





def count_frequency(n,m):
  hash_map = {}
  l=len(n)                                            #tc = o(m+n)
  for i in n:                                         #sc = o(n)
    hash_map[i] = hash_map.get(i,0)+1   
  for i in m:
    if i in hash_map:
      print(hash_map[i])
    else:
      print("0")  
    
count_frequency(n,m)  
