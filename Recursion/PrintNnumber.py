
#tc = o(n+1) similar to o(n)
#sc = o(n+1) similar to o(n)


n = int(input("Enter a number:"))

# def PrintNumbers(n):
#   if n==0:
#     return
#   PrintNumbers(n-1)
#   print(n,end=",")


def PrintNumbers(n):
  if n==0:
    return
  print(n,end=",")
  PrintNumbers(n-1)
  




# i = 1
# def PrintNumbers(i,n):
#   if n<i:
#     return
#   print(i,end=",")
#   PrintNumbers(i+1,n)
  
  
  
PrintNumbers(n)  