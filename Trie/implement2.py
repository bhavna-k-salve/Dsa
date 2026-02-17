


class TrieNode:
  def __init__(self):
    self.children = {}
    self.count_prefix = 0
    self.end_count = 0
    
    
class Trie:
  def __init__(self):
    self.root = TrieNode()
    
  def insert(self,word):
    node = self.root
    for ch in word:
      if ch not in node.children:      
        node.children[ch] = TrieNode()
      node = node.children[ch]  
      node.count_prefix +=1
    node.end_count += 1
    
  
  def countWordEqualTo(self,word):
    node =self.root
    for ch in word:
      if ch not in node.children:
        return 0
      node = node.children[ch]
    return node.end_count  
        
 
  def countStartingWith(self,word):
    node =self.root
    for ch in word:
      if ch not in node.children:
        return 0
      node = node.children[ch]
    return node.count_prefix  


  def erase(self,word):
    node =self.root
    for ch in word:
      if ch not in node.children:
        return
      node = node.children[ch]
      node.count_prefix -= 1
    node.end_count -= 1  
    
    
obj = Trie()
obj.insert("apple")
obj.insert("apple")
obj.insert("app")
obj.insert("application")
obj.erase("app")
print(obj.countWordEqualTo("apple")) 
print(obj.countStartingWith("app")) 
                        