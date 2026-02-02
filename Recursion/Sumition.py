
#tc = o(n+1) similar to o(n)
#sc = o(n+1)  similar to o(n)


n = int(input("Enter a number: "))
def Sum(n):
  if n==1:
    return 1
  return (n+Sum(n-1))
print(Sum(n))





# n = int(input("Enter a number: "))

# def Sum(sum,i,n):
#   if i > n:
#     print(sum)
#     return 
#   Sum(sum+i,i+1,n)

# Sum(0,1,n)