#create Doubly linked list node
class Node:
  def __init__(self,data=None,prev=None,next=None):
    self.prev = prev
    self.data = data
    self.next = next
#create a Deque class to implement deque data structure.
class Deque:
  def __init__(self):
    self.front = None
    self.rear = None
    self.item_count = 0

  def is_empty(self):
    return self.front == None

  def insert_front(self,data):
    n = Node(data)
    if self.is_empty():
      self.front = n
      n.prev = n
      n.next = n
      self.rear = n
    else:
      n.next = self.front
      self.front.prev = n
      n.prev = self.rear
      self.rear.next = n
      self.front = n
    self.item_count += 1  

  def insert_rear(self,data):
    n = Node(data)
    if not self.is_empty():
      if self.front == self.rear:
        self.front.next = n
        n.prev = self.rear
        n.next = self.front
        self.front.prev = n
      else:
        n.prev = self.rear
        n.next = self.front
        self.front.prev = n
        self.rear.next = n
    self.rear = n
    self.item_count += 1 

  def delete_front(self):
    if not self.is_empty():
      self.front.next.prev = self.rear
      self.rear.next = self.front.next
      self.item_count -= 1 

  def delete_rear(self):
    if not self.is_empty():
      self.front.prev = self.rear.prev
      self.rear.prev.next = self.front    
      self.item_count -= 1 

  def get_front(self):
    if not self.is_empty():
      data =  self.front.data
      return data
    
  def get_rear(self):
    if not self.is_empty():
      data =  self.rear.data
      return data  
        
  def size(self):
    return self.item_count


d1 = Deque()        
d1.insert_front(10)
d1.insert_front(20)
d1.insert_rear(30)
d1.insert_rear(40)
d1.delete_front()
print(d1.get_front())
print(d1.get_rear())