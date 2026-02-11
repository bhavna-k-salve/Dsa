




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


def findLastRight(node):
  while node.right is not None:
    node = node.right
  return node  

def deletion(node):
  if node.left is None:
    return  node.right
  elif node.right is None:
    return node.left
  else:
    right_child = node.right
    last_right = findLastRight(node.left)
    last_right.right = right_child
    return node.left
  














    
def delete_node(node,target):
  if node is None:
    return None
  if node.item == target:
    return deletion(node)
  temp = node
  while temp is not None:
    if temp.item > target:
      if temp.left !=None and temp.left.item == target:
        temp.left = deletion(temp.left)
        break
      else:
        temp =temp.left
    else:        
      if temp.right != None and temp.right.item == target:
        temp.right = deletion(temp.right)
        break
      else: 
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
delete_node(n1,10)
print()
pre_order(n1)