

class Node:
  def __init__(self,item=None,next=None):
    self.item =item
    self.next =next
    
    

class SLL:
  def __init__(self,start=None):
    self.start = start
    self.count = 0
  
  def is_Empty(self):
    return self.start==None
  
  def len(self):
    return self.count
    
  def append(self,item):
    n = Node(item)  
    if self.is_Empty():
      self.start = n                               #tc =o( n)
    else:                                      #sc = o(1)
      temp = self.start
      while temp.next != None:
        temp = temp.next 
      temp.next = n 
    self.count+=1 


  def traversal(self):
    if self.is_Empty():
      print("SLL is empty")
    else:
      temp = self.start                                  #tc =o( n)
      while temp.next is not None:                       #sc =o( 1)
        print(temp.item,end=" ")
        temp = temp.next
      print(temp.item)  
      
        
  def insert(self,ind,item):
    con=0
    n =Node(item)
    if ind==0:
      n.next = self.start
      self.start = n
    else:
      prev_node =None                                #tc =o( n)
      temp = self.start                              #sc =o( 1)
      while con != ind and con <= self.count:
        prev_node = temp
        temp = temp.next
        con += 1
      prev_node.next = n
      n.next = temp  
    self.count+=1  
          
  def delete(self,val):
    temp = self.start
    if temp != None:
      if val == temp.item:
        self.start = temp.next  
      else:                                            #tc =o( n)
        prev_node =None                                #sc =o( 1)
        while temp != None:
          if temp.item == val:
            prev_node.next = temp.next        
          prev_node = temp 
          temp = temp.next
    else:
      print("SLL  is empty")    

  
  
  def cycle(self):
    temp =self.start
    # my_dict =dict()
    # travel = 0
    # while temp is not None:                    #tc =o(n)
    #   if temp in my_dict:                      #sc=o(n)
    #     return travel - my_dict[temp]
    #   my_dict[temp] =  travel
    #   travel+=1
    #   temp = temp.next
    # return 0   
    
    slow = temp 
    fast = temp
    while fast != None and fast.next != None:
      slow= slow.next
      fast =fast.next.next                             #tc =o(n)
      if slow == fast:                                 #sc =o(1)
        slow = slow.next
        travel = 0
        while slow != fast:
          count+=1
        return count
    return 0   
      
    

  
  
obj = SLL()
print(obj.cycle())

obj.append(10)
obj.append(2)
obj.append(7)
# obj.delete(2)
obj.insert(1,99)
obj.append(9)





