

#tc = o(n) + o(n) + o(n)
#sc = o(1)


s = "Hello World"




def reverse_Word(s):
  l = s.split()
  result = l[-1::-1]   #l.reverse()
  s = " ".join(result)
  return s


print(reverse_Word(s))  