




#tc =o(n)
#sc = o(1)



class Node:
  def __init__(self,item =None,left=None,right =None):
    self.item = item
    self.left = left
    self.right = right
    
    
 
def morris_traversal(node):
  result = []
  temp = node
  while temp is not None:
    if temp.left is None:
      result.append(temp.item)
      temp = temp.right 
    else:
      predecessor = temp.left
      while predecessor.right is not None and predecessor.right != temp:
        predecessor = predecessor.right 
      if predecessor.right is None:
        predecessor.right = temp
        temp = temp.left
      else:
        predecessor.right = None
        result.append(temp.item)
        temp = temp.right
  return result                                   

 
    
    
    
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



print(morris_traversal(n1))
