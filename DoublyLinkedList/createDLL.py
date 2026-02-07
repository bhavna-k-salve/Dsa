



class Node:
  def __init__(self,item=None,prev=None,next=None):
    self.item = item
    self.prev = prev
    self.next = next
    
 
 
class DLL:
  def __init__(self):
    self.start = None
    self.count = 0
  
  def is_Empty(self):
    return self.start is None
  
    
  def len(self):
    return self.count
  
  
  def insert_at_start(self,item):
    n = Node(item)
    if self.start is None:                                           #tc = o(1)
      self.start = n                                                 #sc = o(1)
    else:
      temp = self.start
      n.next = temp 
      temp.prev = n
      temp = n  
    self.count += 1  
          
  def append(self,item):
    n = Node(item)
    temp = self.start
    if temp is None:                                    #tc = o(n)
      temp = n                                           #sc = o(1)
      return                                     
    else:
      while temp.next:
        temp = temp.next
      temp.next = n
      n.prev = temp 
    
  
  def insert_at(self,item,position):
    n = Node(item)
    if position == 0:
      self.insert_at_start(item)
      return 
    temp = self.start                                   #tc = o(n)
    count = 0                                             #sc = o(1)
    while temp and count < position-1:
      temp = temp.next
      count += 1
    if temp is None:
      print("Position out of bounds.")
      return 
    n.next = temp.next   
    n.prev = temp
    if temp.next:
      temp.next.prev = n
    temp.next = n  
  
  
  
  def traversal(self):
    if self.is_Empty():
      print("DLL is empty") 
      return                                       #tc = o(n)
    temp = self.start                                #sc = o(1)
    while temp:
      print(temp.item,end=" ")
      temp = temp.next
        
    
        
obj = DLL()
obj.insert_at_start(3) 
obj.append(5)  
obj.traversal()               