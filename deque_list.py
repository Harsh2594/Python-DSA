class Deque:
  def __init__(self):
    self.deque = []

  def is_empty(self):
    return len(self.deque) == 0

  def insert_front(self,data):
    if self.is_empty():
      self.deque.append(data)
    else:
      self.deque.insert(0,data)

  def insert_rear(self,data):
    self.deque.append(data)

  def delete_front(self):
    if self.is_empty():
      raise IndexError("List is empty")
    else:
      self.deque.pop(0)

  def delete_rear(self):
    if self.is_empty():
      raise IndexError("List is empty")
    else:
      self.deque.pop(-1)

  def get_front(self):
    if self.is_empty():
      raise IndexError("List is empty")
    else:
      return self.deque[0]
    
  def get_rear(self):
    if self.is_empty():
      raise IndexError("List is empty")
    else:
      return self.deque[-1]  
    
  def size(self):
    return len(self.deque)  


d1 = Deque()
d1.insert_front(10)
d1.insert_front(20)
d1.insert_rear(30)
d1.insert_rear(40)
print(d1.deque)
print(d1.get_front(),d1.get_rear())
d1.delete_front()
print(d1.get_front(),d1.get_rear())
d1.delete_rear()
print(d1.get_front(),d1.get_rear())
