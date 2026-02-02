

#tc = o(2**n)
#sc = o(2**n)


n=int(input("Enter a number:"))


def Fibonacci(n):
  if n==0 or n==1:
    return n
  
  return Fibonacci(n-1)+Fibonacci(n-2)

print(Fibonacci(n))





