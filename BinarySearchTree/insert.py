





#tc =o(log2(n))
#sc = o(1)



class Node:
  def __init__(self,item =None,left=None,right =None):
    self.item = item
    self.left = left
    self.right = right
    


    
def pre_order(node):
  if node == None:
    return 
  print(node.item,end=" ")
  pre_order(node.left)
  pre_order(node.right)    
 
 
 
 
def insert(node,target): 
  new_node = Node(target)
  if node is None:
    return new_node
  temp  =node
  while True:
    if temp.item > target:
      if temp.left is None:
        temp.left =new_node
        break
      temp = temp.left
    else:
      if temp.right is None:
        temp.right = new_node 
        break
      temp = temp.right
  return node
 
  
    
n1 = Node(9)
n2 = Node(3)
n3 = Node(11)   
n4 = Node(2)   
n5 = Node(7)   
n6 = Node(10)   
n7 = Node(15)   
n8 = Node(4)   
n9 = Node(8)   
n10 = Node(14)      




n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7
n5.left = n8
n5.right = n9
n7.left = n10


pre_order(n1)
root = insert(n1,20)
print()
pre_order(root)