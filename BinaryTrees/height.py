





#tc = o(n)
#sc = o(h)


from collections import deque 



class Node:
  def __init__(self,item =None,left=None,right =None):
    self.item = item
    self.left = left
    self.right = right
    
    
  
# def height(node):
#   if node == None:
#     return 0
#   left_height = height(node.left)
#   right_height = height(node.right)  
#   return 1+ max(left_height,right_height)
   









#tc = o(n)
#sc = o(n)

  
def height(node):
  queue = deque([])
  height = 0
  queue.append(node)
  while len(queue) != 0:
    level_size = len(queue)
    height += 1
    for _ in range(level_size):
      e = queue.popleft()
      if e.left is not None:
        queue.append(e.left)
      if e.left is not None:
        queue.append(e.right)
  return height   
 
  
p1 = Node(5) 
p2 = Node(3) 
p3 = Node(4) 
p4 = Node(2) 
p5 = Node(9) 
p6 = Node(8) 
p7 = Node(10)
p8 = Node(1)
p9 = Node(6)

p1.left = p2
p1.right = p3 
p2.left = p4 
p2.right = p5
p3.left = p6
p3.right = p7
p6.left = p8
p6.right = p9  
      
    
print(height(p1))    
        