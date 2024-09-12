from linked_list import *
class Stack:
  def __init__(self):
    self.my_list = SLL()
    self.item_count = 0

  def is_empty(self):
    return self.my_list.is_empty()
  
  def push(self,data):
    self.my_list.insert_at_start(data)
    self.item_count += 1
    
  def pop(self):
    if not self.is_empty():
      self.my_list.delete_first()
      self.item_count-=1
  
  def peek(self):
    if not self.is_empty():
      return self.my_list.head.data
    else:
      raise self.is_empty()

  def size(self):
    return self.item_count

s1 = Stack()
s1.push(10)
s1.push(20)
s1.push(30)
print(s1.size())
print(f"Top element in stack = {s1.peek()}")
s1.pop()
print(f"Top element in stack = {s1.peek()}")

