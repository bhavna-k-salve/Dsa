






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
      temp = n 
      return                                     #sc = o(1)
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
    temp = self.start
    while temp:
      print(temp.item,end="")
      temp = temp.next
   
   
  def findPair(self,target):
    # temp1 =   self.start
    # result =[]
    # while temp1 is not None:                                #tc = o(n(n+1)/2)similar to o(n²)
    #   temp2 = temp1.next                                    #sc = o(1)
    #   while temp2 is not None:
    #     if temp1.item + temp2.item == target:
    #       result.append([temp1.item,temp2.item])
    #     temp2 = temp2.next
    #   temp1 = temp1.next    
    # return result  
    
    # temp = self.start
    # result = []
    # mySet =set()
    # while temp is not None:                              #tc = o(n)
    #   remaining = target - temp.item                    #sc = o(n)
    #   if remaining in mySet:
    #     result.append([temp.item,remaining])
    #   mySet.add(temp.item)
    #   temp=temp.next   
    # return result   
    
    result = []
    left = self.start
    right = self.start 
    while right.next is not None:
      right =right.next
    while left is not None and right is not None and left.item < right.item:
      total = left.item + right.item
      if total == target:                                     #tc = o(2n) similar to o(n)
        result.append([left.item,right.item])                 #sc = o(1)
        left = left.next
        right = right.prev
      elif total > target:
        right= right.prev
      else:
        left = left.next
    return result      
    
    
      
    
        
obj = DLL()
obj.insert_at_start(1) 
obj.append(2)  
obj.append(3)  
obj.append(4) 
obj.append(5) 
obj.append(6) 
obj.append(7) 
print(obj.findPair(8))              