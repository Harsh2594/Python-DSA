class Stack(list):
  #self is object of stack class which is child of list class
  def is_empty(self):
    return len(self) == 0
  
  def push(self,data):
    self.append(data)

  def pop(self):
    if not self.is_empty():
      return self.pop()  
    else:
      raise IndexError("Stack is empty")
  
  def peek(self):
    if not self.is_empty():
      return self[-1]
    else:
      return IndexError("Stack is empty")
    
  def size(self):
    return len(self)

#Implement a way to restrict use of insert() method of list class from stack object.

  def insert(self,index,data):
    raise AttributeError("No Attribute 'insert' in stack")




s1 = Stack()
#s1.insert(0,10) #raise exception 
s1.push(10)
s1.push(20)
s1.push(30)
print(s1.peek())  



