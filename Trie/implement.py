

# class TrieNode:
#   def __init__(self):
#     self.children = {}
#     self.is_end =False


# #sc = o(N*L)
# class Trie:
#   def __init__(self):
#     self.root = TrieNode()
    
#    #tc =o(L) 
#   def insert(self,word):
#     node = self.root
#     for char in word:
#       if char not in node.children:
#         node.children[char] = TrieNode()
#       node = node.children[char]
#     node.is_end = True     
    
#   #tc = o(L)  
#   def search(self,word):
#     node = self.root
#     for char in word:
#       if char not in node.children:
#         return False
#       node = node.children[char]
#     return node.is_end
  
#   #tc =o(L)
#   def startsWith(self,prefix):
#     node = self.root
#     for char in prefix:
#       if char not in node.children:
#         return False
#       node = node.children[char]
#     return True
  
  
# trie = Trie()
# trie.insert("apple")
# trie.insert("app")
# print(trie.search("app"))
# print(trie.search("apz"))
# print(trie.startsWith("ap"))

        
        



#tc = o(l)
#sc = o(l*n)

class TrieNode():
  def __init__(self):
    self.children = {}
    self.is_end = False
    
    
    
class Trie():
  def __init__(self):
    self.root = TrieNode()
    
  def insert(self,word):
    node =self.root
    for ch in word:
      if ch not in node.children:
        node.children[ch] = TrieNode()
      node = node.children[ch]
    node.is_end = True
    
    
  def search(self,word):
    node = self.root
    for ch in word:
      if ch not in node.children:
        return False
      node = node.children[ch]
    return True
  
  
  def startwith(self,word):
    node = self.root
    for ch in word:
      if ch not in node.children:
        return False
      node = node.children[ch]
    return True  
          
    
    
    
    
obj = Trie()
print(obj.search("apple"))
obj.insert("apple")
obj.insert("app")
obj.insert("application")  
print(obj.search("apple")) 
print(obj.startwith("aplica")) 
                    
        