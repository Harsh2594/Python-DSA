class PriorityQueue:
  def __init__(self):
    self.queue = []
  
  def is_empty(self):
    return len(self.queue) == 0

  def push(self,data,priority):
    index = 0
    while index<len(self.queue) and self.queue[index][1] <= priority:
      index += 1
    self.queue.insert(index,(data,priority))  
    
  def pop(self):
    if self.is_empty():
      raise IndexError("Queue has no item")
    return self.queue.pop(0)[0]

  def size(self):
    return len(self.queue)


p1 = PriorityQueue()
p1.push(11,4)
p1.push(20,1)
p1.push(3,2)
p1.push(45,3)
p1.push(55,3)
p1.push(100,0)
print(p1.queue)

while not p1.is_empty():
  print(p1.pop())
