#Implement Queue data Structure:
class Queue:
  def __init__(self):
    self.queue = []
    self.item_count = 0

  def is_empty(self):
    return self.queue == None
#enqueue: Add item in queue
  def enqueue(self,data):
    self.queue.append(data)
    self.item_count += 1
#dequeue: Remove first element of queue
  def dequeue(self):
    if not self.is_empty():
      self.queue.pop(0)
      self.item_count -= 1
    else:
      raise Exception("Stack is empty, Can not dequeue")

  def get_front(self):
    if self.is_empty():
      raise Exception("Stack is empty, Can not get value")
    else:
      return self.queue[0]

  def get_rear(self):
    if self.is_empty():
      raise Exception("Stack is empty, Can not get value")
    else:
      return self.queue[-1]
    
  def size(self):
    return self.item_count
  

q1 = Queue()
q1.enqueue(11)
q1.enqueue(12)
q1.enqueue(13)
q1.enqueue(14)
print(q1.queue)
q1.dequeue()
print(q1.queue)
print(f"Get front element of queue = {q1.get_front()}")
print(f"Get rear element of queue = {q1.get_rear()}")
print(q1.size())
