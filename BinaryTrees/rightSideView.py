





#tc = o(n)
#sc = o(n)+o(n)

from collections import deque 


class Node:
  def __init__(self,item =None,left=None,right =None):
    self.item = item
    self.left = left
    self.right = right
    
  
# def right_view(node):
#   queue = deque([])
#   result = []
#   queue.append(node)
#   while len(queue) != 0:
#     level_size = len(queue)
#     for i in range(level_size):
#       e = queue.popleft()
#       if i == level_size-1:
#         result.append(e.item)
#       if e.left :
#         queue.append(e.left)
#       if e.right :
#         queue.append(e.right)  
#   return result   











#tc =o(n)
#sc =o(h)

   
def reverse_post_order(node,level,ans):
  if node == None:
    return 
  if len(ans)==level:
    ans.append(node.item)
  if node.right:
    reverse_post_order(node.right,level+1,ans)
  if node.left:  
    reverse_post_order(node.left,level+1,ans)
  
 
def right_view(node):
  ans = []
  reverse_post_order(node,0,ans)
  return ans





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
      
    
print(right_view(p1) )   
        