#Implement priority queue using linked list:
class Node:
  def __init__(self, data = None, priority = None, next = None):
    self.data = data
    self.priority = priority
    self.next = next

class PriorityQueue:
  def __init__(self):
    self.start = None
    self.item_count = 0
  
  def is_empty(self):
    return self.start == None


  def push(self,data,priority):
    n = Node(data,priority)
    if self.is_empty():
      self.start = n
    elif priority < self.start.priority:
      n.next = self.start
      self.start = n  
    else:
      temp = self.start
      while priority > temp.next.priority:
        temp = temp.next
      n.next = temp.next
      temp.next = n  
    self.item_count += 1  
    
#function to return highest priority data:    
  def pop(self):
    if self.is_empty():
      raise IndexError("Stack is empty")
    else:
      data = self.start.data
      self.start = self.start.next
      self.item_count -= 1  
      return data
    
  def size(self):
    return self.item_count    
        
p1 = PriorityQueue()
p1.push("task5",5)
p1.push("task3",3)
p1.push("task2",2)
p1.push("task1",1)
p1.push("task4",4)
print(p1.pop())
print(p1.size())

