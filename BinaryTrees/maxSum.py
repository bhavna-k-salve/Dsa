




#tc = o(n)
#sc = o(h)




class Node:
  def __init__(self,item =None,left=None,right =None):
    self.item = item
    self.left = left
    self.right = right
    
    
maximum = float("-inf")    
def max_sum(node):
  global maximum
  if node == None:
    return 0
  left_sum = max_sum(node.left)
  if left_sum < 0:
    left_sum = 0
  right_sum = max_sum(node.right) 
  if right_sum < 0:
    right_sum = 0
  maximum =  max(maximum,left_sum + right_sum + node.item)
  return node.item + max(left_sum,right_sum)  

 

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
    
max_sum(p1) 
print(maximum)   
        