#Stack Implementation by inheriting SLL class
from linked_list import *
class Stack(SLL):
  
  item_count = 0

  def is_empty(self):
    return super().is_empty()
  
  def push(self,data):
    self.insert_at_start(data)
    self.item_count+=1

  def pop(self):
      if not self.is_empty():
        self.delete_first()
        self.item_count-=1

  def peek(self):
    if not self.is_empty():
      return self.head.data
    else:
      raise self.is_empty()
    
  def size(self):
    return self.item_count
  

s1 = Stack()
s1.push(5)
s1.push(10)
s1.push(15)
print(f"Top element in stack = {s1.peek()}")
print(s1.size())
s1.pop()
print(f"Top element in stack = {s1.peek()}")
print(s1.size())


    