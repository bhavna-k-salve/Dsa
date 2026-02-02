
#tc = o(n+1) similar to o(n)
#sc = o(n+1) similar to o(n)


x =int (input("Enter a number:"))
n = int(input("how many time you want to print:"))

# def func(x,n):
#   if n == 0:
#     return 
#   print(x)
#   func(x,n-1)

def func(x,n):
  if n == 0:
    return 
  func(x-1,n-1)
  print(x)
  
func(x,n)  