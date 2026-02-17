
# #tc = o(n(n+1)/2) similarr to o(n²)
# #sc = o(n²)


# def count_distinct(s):
#   n =len(s)
#   my_set = set()
#   for i in range(0,n):
#     st = ""
#     for j in range(i,n):
#       st += s[j]
#       my_set.add(st)
#   return len(my_set)+1    


# print(count_distinct("abab"))












#tc = o(n²)
#sc = o(n²)

class Trienode:
  def __init__(self):
    self.children = {}
    
    
class Trie:
  def __init__(self):
    self.root = Trienode()
    self.count =0
  
  
  def count_dictinct(self,word):
    n = len(word)
    for i in range(n):
      node = self.root
      for j in range(i,n):
        ch = word[j]
        if ch not in node.children:
          node.children[ch] = Trienode()
          self.count += 1
        node = node.children[ch]  

    return self.count+1
  
  
  
obj = Trie()
print(obj.count_dictinct("ababa"))     