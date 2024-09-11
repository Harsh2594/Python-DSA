class StackList:
  def __init__(self):
    self.stack = []

  def is_empty(self):
    return len(self.stack) == 0

  def push(self,data):
    self.stack.append(data)

#delete last element and also return its value:    
  def pop(self):
    if not self.is_empty():
      return self.pop()
    else:
      raise IndexError("Stack is empty")
  #this method only return last element of stack without removing it.
  def peek(self):
    if not self.is_empty():
      return self.stack[-1]
    else:
      raise IndexError("Stack is empty")
    
  def size(self):
    return len(self.stack)
  
  


s1 = StackList()
s1.push(10)
s1.push(20)
s1.push(30)
print(s1.peek())