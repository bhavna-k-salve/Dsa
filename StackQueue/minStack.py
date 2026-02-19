





class Stack:
  def __init__(self):
    self.items = []
    self.min = float("inf")
    
  def is_empty(self):
    return len(self.items) == 0                         #tc=o(1)
  
  def push(self,item):
    self.items.append(item)                             #tc=o(1)
    self.min = min(self.min,item)
    
  def pop(self):
    if self.is_empty():
      return "Cannot pop,stack is empty."               #tc=o(1)
    x = self.items.pop()
    return x
  
  def get_min(self): 
    if self.is_empty():
      return 0                                          #tc =o(1)
    return self.min
  
  def top(self):
    if self.is_empty():
      return "Cannot top, stack is empty"               #tc=o(1)
    return self.items[-1]    
  
  def size(self):
    return len(self.items)                              #tc=o(1)
  
  
  
stack = Stack()
stack.push(5)
stack.push(1)
stack.push(10)
stack.push(15)
print(stack.pop())
print(stack.top())
print(stack.is_empty())  
print(stack.get_min())