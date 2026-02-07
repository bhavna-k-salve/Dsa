






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
      self.start = n                                             #sc = o(1)
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
      temp = n                                          #sc = o(1)
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
      return
    temp = self.start                              #tc =o(n)
    while temp:                                    #sc =o(1)
      print(temp.item,end=" ")
      temp = temp.next
    print()    
  
  
  def reverse(self):
    # temp = self.start
    # stack = []
    # while temp is not None:
    #   stack.append(temp.item)
    #   temp = temp.next                    #tc =o(2n)
    # temp = self.start                      #sc =o(n)
    # while temp is not None:
    #   e = stack.pop()
    #   temp.item = e
    #   temp =temp.next
    
    temp = self.start
    if temp.next is  None:
      return temp
    prev = None
    while temp is not None:
      front = temp.next
      temp.next = prev                     #tc = o(n)
      temp.prev = front                    #sc = o(1)
      prev = temp
      temp = front
    self.start = prev  
    return self.traversal()
  
  
  
        
obj = DLL()
obj.insert_at_start(3) 
obj.append(5)  
obj.append(8) 
obj.append(11) 
obj.append(24) 
obj.append(45) 
obj.traversal()    
obj.reverse()    
 