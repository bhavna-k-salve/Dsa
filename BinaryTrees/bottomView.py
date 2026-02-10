




#tc = o(n + nlogn + n)
#sc = o(n) +o(n)

from collections import deque 


class Node:
  def __init__(self,item =None,left=None,right =None):
    self.item = item
    self.left = left
    self.right = right
    
    
    
def bottom_view(node):
  if not node:
    return None
  ans = []
  queue = deque()  
  result ={}
  queue.append((node,0))
  while queue:
    e,line = queue.popleft()
    result[line] = e.item
    if e.left:
      queue.append((e.left,line-1))  
    if e.right:
      queue.append((e.right,line+1))
  for value in sorted(result.items()):
    ans.append(value[1])
  return ans          
 
  
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
      
    
print(bottom_view(p1) )   
        