class Node:
  def __init__(self,data=None,next=None):
    self.data = data
    self.next = next

class Stack:
  def __init__(self):
    self.top = None
    self.item_count = 0

  def is_empty(self):
    return self.top == None

  def push(self,data):
    n = Node(data)
    n.next = self.top
    self.top = n
    self.item_count += 1
  
  def pop(self):
    if not self.is_empty():
      data = self.top.data
      self.top = self.top.next
      self.item_count -=1
      return data
    else:
      raise IndexError("Stack is empty")
    
  def peek(self):
    if not self.is_empty():
      return self.top.data
    else:
      raise self.is_empty()
    
  def size(self):
    return self.item_count
  
s1 = Stack()
s1.push(10)  
s1.push(20)  
s1.push(30)  
print(f"total element in stack = {s1.size()}")
print(f"top element in the stack = {s1.peek()}")
print(f"poped element = {s1.pop()}")
print(f"total element in stack = {s1.size()}")
print(f"top element in the stack = {s1.peek()}")

  



