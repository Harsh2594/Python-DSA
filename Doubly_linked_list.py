class Node:
  def __init__(self,data=None,next=None,prev=None):
    self.data = data
    self.prev = prev
    self.next = next

class DLL:
  #constructor
  def __init__(self,head = None):
    self.head = head
  #Check list is empty or not
  def is_empty(self):
    return self.head == None
  #insert data at start or add first node to head
  def insert_at_start(self,data):
    if self.head == None:
      my_node = Node(data)
      self.head = my_node
    else:
      my_node = Node(data)
      my_node.next = self.head
      self.head = my_node

  def insert_at_last(self,data):
    my_node = Node(data)
    if self.is_empty():
      self.head = my_node
    else:
      temp = self.head
      while temp.next != None:
        temp = temp.next
      my_node.prev = temp  
      temp.next = my_node
      
  #serach any item in list
  def search_item(self,data):
    temp = self.head
    while temp is not None:
      if temp.data == data:
        return temp
      temp = temp.next
    return None
  #print all list element in sequence 
  def print_list(self):
    temp = self.head
    while temp is not None:
      print(temp.data,end=" ")
      temp = temp.next
    print()    
  #Insert a node after given list item
  def insert_after(self,temp,data):
    if temp is not None:
      my_node = Node(data,temp.next,temp)
      if temp.next is not None:
        temp.next = my_node

  def delete_first(self):
    temp = self.head
    self.head = temp.next      

  def delete_last(self):
    if self.head is None:
      pass
    elif self.head.next == None:
      self.head = None
    else:
      temp = self.head
      while temp.next is not None:
        temp = temp.next
      temp.prev.next = None    
    
  
  def delete_item(self,temp):
    if temp.next is not None:
      temp.next.prev = temp.prev
    if temp.prev is not None:
      temp.prev.next = temp.next
    else:
      self.head = temp.next

#Implement iterator for DLL class to access all element of list in a sequence:

  def __iter__(self):
    return DLLIterator(self.head)

class DLLIterator:
  def __init__(self,head):
    self.current = head

  def __iter__(self):
    return self

  def __next__(self):
    if not self.current:
      raise StopIteration
    data = self.current.data
    self.current = self.current.next
    return data           

    

#driver code_
#check all methods:

#make class object
my_list = DLL()
#-----------insert data------------------
my_list.insert_at_start(10)
my_list.insert_at_last(20)
my_list.insert_at_start(0)
my_list.insert_after(my_list.search_item(10),15)
#-------------print list item-------------
#my_list.print_list()
#-----------check methods-----------------
#my_list.delete_last()
#my_list.delete_item(my_list.search_item(15))
#my_list.print_list()
#-----------check Iterator class---------
#for x in my_list:
#  print(x)
#print()  



