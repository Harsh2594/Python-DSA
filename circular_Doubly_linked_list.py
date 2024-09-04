#Create Node with previous and next reference attributes
class Node:
  def __init__(self,data = None,prev = None,next = None):
    self.data = data
    self.prev = prev
    self.next = next

class CDLL:
  def __init__(self,head=None):
    self.head = head

  def is_empty(self):
    return self.head == None

  def insert_at_first(self,data):
    n = Node(data)
    if self.is_empty():
      n.next = n
      n.prev = n
    else:
      n.next = self.head
      n.prev = self.head.prev
      self.head.prev.next = n
      self.head.prev = n
    self.head = n  

  def insert_at_last(self,data):
    n = Node(data)
    if self.is_empty():
      n.next = self.head
      n.prev = self.head
      self.head = n
    else:
      n.next = self.head
      n.prev = self.head.prev
      n.prev.next = n
      self.head.prev = n
      
  def search_item(self,data):
    temp = self.head
    if temp == None:
      return None
    if temp.data == data:
      return temp
    else:
        temp = temp.next
    while temp is not self.head:
      if temp.data == data:
        return temp
      temp = temp.next
    return None
    
  def insert_after(self,temp,data):
    if temp is not None:
      n = Node(data)
      n.next = temp.next
      n.prev = temp
      temp.next.prev = n
      temp.next =n

  def print_list(self):
    temp = self.head
    while True:
      print(temp.data,end=" ")
      temp = temp.next
      if temp == self.head:
        break
    print()

  def delete_first(self):
    temp = self.head
    temp.next.prev = temp.prev
    temp.prev.next = temp.next
    self.head = temp.next

  def delete_last(self):
    temp = self.head
    temp.prev.prev.next = self.head
    temp.prev = self.head.prev.prev

  def delete_item(self,data):
    if not self.is_empty():
      if self.head.next == self.head:
        if self.head.data == data:
          self.head = None
      else:
        if self.head.prev.data == data:
          self.delete_last()
        else:
          temp = self.head
          if temp.data == data:
            self.delete_first()
          else:
            temp = temp.next
            while temp.next != self.head:
              if temp.data == data:
                temp.prev.next = temp.next
                temp.next.prev = temp.prev
                break
              temp = temp.next        

  def __iter__(self):
    if self.head == None:
      return CDLLIterator(None)
    else:
      return CDLLIterator(self.head)
    
class CDLLIterator:
  def __init__(self,head):
    self.current = head
    self.start = head
    self.count = 0

  def __iter__(self):
    return self

  def __next__(self):
    if self.current == None:
      raise StopIteration
    if self.current == self.start and self.count==1:
      raise StopIteration  
    else:
      self.count = 1
      data = self.current.data
      self.current = self.current.next
      return data

#Driver Code:

my_list = CDLL()
my_list.insert_at_first(15)
#my_list.insert_at_first(0)
#my_list.insert_after(my_list.search_item(10),15)
my_list.insert_at_first(10)
my_list.insert_at_first(5)
my_list.insert_after(my_list.search_item(10),14)
#my_list.print_list()
#my_list.delete_last()#my_list.delete_first()
#my_list.delete_item(14)
my_list.print_list()
for x in my_list:
  print(x,end=" ")
  print()          

