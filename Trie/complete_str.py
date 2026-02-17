




class TrieNode:
  def __init__(self):
    self.children = {}
    self.is_end = False
    
    
    
class Trie:
  def __init__(self):
    self.root = TrieNode()
    
  def insert(self,word):
    node = self.root
    for ch in word:
      if ch not in node.children:
        node.children[ch] = TrieNode()
      node = node.children[ch]
    node.is_end = True
  
  
  def check_all_prefix(self,word):
    node = self.root
    for ch in word:
      if ch not in node.children:
        return False
      node = node.children[ch]
      if not node.is_end:
        return False
    return True
  





#tc = o(n*l)+(n*l)
#sc = o(n*l)
  
def completeString(l):
  trie = Trie()
  for word in l:
    trie.insert(word)
  
  best_word = ""
  for word in l:
    if trie.check_all_prefix(word) == True:
      if len(word) > len(best_word) or (len(word)==len(best_word) and word<best_word):
        best_word = word       
  if best_word == "":
    return None
  return best_word       
                 
    
    
l = ["n","ni","nin","ninj","ninjb","ninjc"]

print(completeString(l)) 