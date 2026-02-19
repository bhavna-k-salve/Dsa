


class Queue:
  def __init__(self):
    self.items = []
    
  def is_empty(self):
    return len(self.items) == 0                      #tc=o(1)
  
  def enqueue(self,item):
    self.items.append(item)                         #tc=o(1)
    
  def dequeue(self):
    if self.is_empty():                              #tc=o(n)
      print("dequeue from empty queue")
      return 
    x =self.items.pop(0)
    return x
  
  def front(self):
    if self.is_empty():
      print("cannot peek, queue is empty.")           #tc=o(1)
      return 
    return self.items[0]
  
  def rear(self):
    if self.is_empty():
      print("cannot read, queue is empty")             #tc=o(1)
    return self.items[-1]
  
  def size(self):
    return len(self.items)                                 #tc=o(1)
  
  
  
  
queue = Queue()
queue.enqueue(23)
queue.enqueue(5)
queue.enqueue(15)
queue.enqueue(30)
print(queue.size())
print(queue.front())
print(queue.rear())
print(queue.dequeue())
print(queue.dequeue())
print(queue.front())
print(queue.rear())
print(queue.is_empty())  
         