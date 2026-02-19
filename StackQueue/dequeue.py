


class Node:
  def __init__(self,item = None,next = None,prev = None):
    self.item = item
    self.next = next
    self.prev = prev
    
    
    
class Dequeue:
  def __init__(self):
    self.head = None
    self.tail = None
    self.count = 0
    
  def is_empty(self):
    return self.count == 0        
  
  def push(self,item):
    n = Node(item)
    if self.is_empty():
      self.start = n
      self.tail = n
    else:
      n.prev = self.tail
      self.tail.next = n
      self.tail = n  
    self.count+=1

  def pop(self):
    if self.is_empty():
      return "list is empty"
    pop_value = self.start.item
    self.start.next.prev = None
    self.start = self.start.next
    self.count -= 1
    return pop_value

  def traverse(self):
    temp  =self.start
    while temp != None:
      print(temp.item,end=" ,")
      temp = temp.next
      
  def size(self):
    return self.count    
      
obj = Dequeue()
obj.push(12)
obj.push(34)
obj.push(45)
obj.push(29)
print(obj.size())
obj.traverse()
print()
print(obj.pop())
print(obj.size())
obj.traverse()