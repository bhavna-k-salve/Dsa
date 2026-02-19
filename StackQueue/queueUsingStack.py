


class QueueUsingStack:
  def __init__(self):
    self.st1 = []
    self.st2 = []
    
  def push(self,x):
    while self.st1:
      self.st2.append(self.st1.pop())
    self.st1.append(x)
    while self.st2:
      self.st1.append(self.st2.pop())
      
  def pop(self):
    if not self.st1:
      print("queue is empty")
      return -1
    top_element = self.st1.pop()
    return top_element
  
  def peek(self):
    if not self.st1:
      print("queue is empty")
      return -1
    return self.st1[-1]
  
  def is_empty(self):
    return not self.st1 
  
  
  
  
  
 
  
obj = QueueUsingStack()
obj.push(400)
obj.push(300)
obj.push(200)
obj.push(100)

print(obj.peek())
print(obj.pop())
print(obj.pop())
print(obj.peek())
obj.push(5)
print(obj.peek())
print(obj.st1)
 
         