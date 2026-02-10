




class Node:
  def __init__(self,item =None,left=None,right =None):
    self.item = item
    self.left = left
    self.right = right
    
  
  
drink = Node("drinks") 
hot = Node("hot") 
cold = Node("cold") 
tea = Node("tea") 
coffee = Node("coffee") 
cola = Node("cola") 
fanta = Node("fanta")


drink.left = hot
drink.right = cold

hot.left = tea
hot.right = coffee

cold.left = cola
cold.right =fanta     
    
    
    
print(drink.item)
print(drink.left)
print(hot)
print(drink.right.item)    
    