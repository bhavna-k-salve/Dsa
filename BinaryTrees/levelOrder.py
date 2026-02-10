





#tc = o(n)
#sc = o(n)

from collections import deque 


class Node:
  def __init__(self,item =None,left=None,right =None):
    self.item = item
    self.left = left
    self.right = right
    
  
def level_order(node):
  queue = deque([])
  result = []
  queue.append(node)
  while len(queue) != 0:
    e = queue.popleft()
    result.append(e.item)
    if e.left is not None:
      queue.append(e.left)
    if e.left is not None:
      queue.append(e.right)
  return result   

p1 = Node(1) 
p2 = Node(2) 
p3 = Node(3) 
p4 = Node(4) 
p5 = Node(5) 
p6 = Node(6) 
p7 = Node(7)
p8 = Node(8)
p9 = Node(9)
p1.left = p2
p1.right = p3 
p2.left = p4 
p2.right = p5
p3.left = p6
p3.right = p7
p6.left = p8
p6.right = p9  
      
    
print(level_order(p1) )   
        