

#tc = o(n)
#sc = o(n)


n = int(input("Enter a number:"))
def factorial(n):
  if n==1 or n==0:
    return 1
  return (n * factorial(n-1))

print(factorial(n))