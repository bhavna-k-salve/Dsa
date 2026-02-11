

#tc = o(n)
#sc = o(n)




class Node:
  def __init__(self,item =None,left=None,right =None):
    self.item = item
    self.left = left
    self.right = right
    
    
    


def solution(node,limit):
  if node is None:
    return True
  if not limit[0] < node.item < limit[1]:
    return False
  
  left = solution(node.left,[limit[0],node.item])
  if left == False:
    return False
  right = solution(node.right,[node.item,limit[1]])
  return left and right    


def isValidBST(node):
  return solution(node,[float("-inf"),float("inf")])



  
    
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
    
    
    
print(isValidBST(n1))    