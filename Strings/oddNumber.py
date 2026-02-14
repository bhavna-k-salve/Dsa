

#tc = o(n)
#sc = o(1)

s = "345768"


def odd_number(s):
  t = int(s)
  l = len(s)
  for i in range(l-1,-1,-1) :
    if t%2==0:
      t = t//10
    else:
      return str(t)
  return " "


print(odd_number(s))   