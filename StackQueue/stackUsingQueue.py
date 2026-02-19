




from collections import deque

class StackUsingQueue:
  def __init__(self):
    self.queue = deque()
    
  def push(self,item):
    self.queue.append(item)
    for _ in range(len(self.queue)- 1):
      self.queue.append(self.queue.popleft())
      
  def pop(self):
    if len(self.queue)==0:
      return "Stack is empty"
    return self.queue.popleft()
  
  def peek(self):
    if len(self.queue) == 0:
      return "Satck is empty"
    return self.queue[0]
  
  def is_empty(self):
    return len(self.queue) == 0
  
  def size(self):
    return len(self.queue)
  
  
  
  
  
obj = StackUsingQueue()
obj.push(400)
obj.push(300)
obj.push(200)
obj.push(100)
print(obj.queue)
print(obj.peek())
print(obj.pop())
print(obj.pop())
print(obj.peek())
obj.push(5)
print(obj.queue)
print(obj.peek())
print(obj.pop())  
print(obj.queue)