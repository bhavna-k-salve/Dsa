






#tc = o(n)
#sc = o(h)




class Node:
  def __init__(self,item =None,left=None,right =None):
    self.item = item
    self.left = left
    self.right = right
    
    
    
def balanced_binary_tree(node):
  if node == None:
    return 0
  left_height = balanced_binary_tree(node.left)
  if left_height == -1:
    return -1
  right_height = balanced_binary_tree(node.right)  
  if right_height == -1:
    return -1
  if abs(left_height-right_height) >1:
    return -1
  return 1+ max(left_height,right_height)
       

 
  
p1 = Node(5) 
p2 = Node(3) 
p3 = Node(4) 
p4 = Node(2) 
p5 = Node(9) 
p6 = Node(8) 
p7 = Node(10)
p8 = Node(1)
p9 = Node(6)
p10= Node(11)

p1.left = p2
p1.right = p3 
p2.left = p4 
p2.right = p5
p3.left = p6
p3.right = p7
p6.left = p8
p6.right = p9  
p9.left = p10
      
    
result = balanced_binary_tree(p1)    
if result == -1:
  print("False")
else:
  print("True")          