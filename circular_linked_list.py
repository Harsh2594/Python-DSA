class Node:
  def __init__(self,data=None,next=None):
    self.data = data
    self.next = next

class CLL:
  def __init__(self,Tail = None):
    self.Tail = Tail

  def is_empty(self):
    return self.Tail == None

  def inser_at_start(self,data):
    if self.Tail == None:
      n = Node(data)
      self.Tail = n
      n.next = n
    else:
      temp = self.Tail
      n = Node(data)
      n.next = temp.next
      temp.next = n

  def insert_at_last(self,data):
    temp = self.Tail
    n = Node(data)
    n.next = temp.next
    temp.next = n
    self.Tail = n

  def search_item(self,data):
    if self.Tail == None:
      print("list is empty")
    else:
      temp = self.Tail.next # Start from the node after Tail (which is effectively the head)
      while True:
        if temp.data == data:
          return temp
        temp = temp.next
        if temp == self.Tail.next: # If we've circled back to the start node, break the loop
          break
      return None  # If we've circled back to the start node, break the loop
        
  def insert_after(self,temp,data):
    if temp == self.Tail:
      n = Node(data,temp.next)
      temp.next = n
      self.Tail = n
    else:
      n = Node(data,temp.next)
      temp.next = n  
  def delete_first(self):
    temp = self.Tail
    temp.next = temp.next.next

  def delete_last(self):
    if not self.is_empty():
      if self.Tail.next == self.Tail:
        self.Tail = None
      else:  
        temp = self.Tail.next
        while temp.next != self.Tail:
          temp = temp.next
        temp.next = self.Tail.next
        self.Tail = temp

  def delete_item(self,data):
    if not self.is_empty():
      if self.Tail.next == self.Tail:
        if self.Tail.data == data:
          self.Tail = None
      else:
        if self.Tail.next.data == data:
          self.delete_first()
        else:  
          temp = self.Tail.next
          while temp != self.Tail:
            if temp.next == self.Tail:
              if self.Tail.data == data:
                self.delete_last()
              break
            if temp.next.data == data:
              temp.next = temp.next.next
              break
            temp = temp.next
          
  def print_list(self):
    if self.is_empty():
      print("list is empty")
      return
    temp = self.Tail
    while True:
      print(temp.next.data,end=" ")
      temp = temp.next
      if temp == self.Tail:
        break
    print()
  
  def __iter__(self):
    if self.Tail == None:
      return CLLIterator(None)
    else:
      return CLLIterator(self.Tail.next)

class CLLIterator:
  def __init__(self,head):
    self.current = head
    self.head = head
    self.count = 0
  def __iter__(self):
    return self
  def __next__(self):
    if self.current == None:
      raise StopIteration
    if self.current == self.head and self.count == 1:
      raise StopIteration
    else:
      self.count = 1
    data = self.current.data
    self.current = self.current.next
    
    return data






my_list = CLL()
my_list.inser_at_start(10)
my_list.insert_at_last(20)
my_list.insert_at_last(30)
my_list.inser_at_start(5)
#my_list.insert_after(my_list.search_item(30),0)
#my_list.insert_after(my_list.search_item(10),15)
#my_list.delete_first()
#my_list.delete_last()
#my_list.delete_item(20)
my_list.print_list()
#print(my_list.search_item(30))
for x in my_list:
  print(x,end=" ")
  print()
      


