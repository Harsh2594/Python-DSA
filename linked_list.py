#How to define a Node
class Node:
  def __init__(self,data = None,next = None):
    self.data = data
    self.next = next
#method for setting the data field of the node
  def setData(self,data):
    self.data = data
#method for getting the data field of the node
  def getData(self,data):
    return self.data
#method for getting the next field of the node
  def getNext(self,next):
    return self.next

  
#Define Singly linked list to create and initialise head variable

class SLL():
  def __init__(self,head = None):
    self.head = head
  
  def is_empty(self):
    return self.head == None
      
  def insert_at_start(self,data):
    my_node = Node(data)
    self.head = my_node
    
  def insert_at_last(self,data):
    my_node = Node(data)
    if self.is_empty():
      self.head = my_node
    else:
      temp = self.head
      while temp.next != None:
        temp = temp.next
      temp.next = my_node  

  def search_ele(self,item):
    temp = self.head
    while temp is not None:
      if temp.data == item:
        return temp
      temp = temp.next
    return None

  def insert_after(self,temp,item):
    if temp is not None:
      my_node = Node(item,temp.next)
      temp.next = my_node
  
  def print_list(self):
    temp = self.head
    while temp is not None:
      print(temp.data,end=" ")
      temp = temp.next
    print()  
 
  def delete_first(self):
    temp = self.head
    self.head = temp.next
    
  def delete_last(self):
    temp = self.head
    while temp.next.next != None:
      temp = temp.next
    temp.next = None  
      
  def delete_item(self,item):
    temp = self.head
    while temp.next != None:
      if temp.next.data == item:
        temp.next = temp.next.next
        return
      temp = temp.next
    else:
      print("item not in list")  
    






#driver code
my_list = SLL()
my_list.insert_at_start(10)
my_list.insert_at_last(30)
my_list.insert_after(my_list.search_ele(10),20)
print(my_list.search_ele(20).data)
my_list.print_list()

#check all methods:

#my_list.delete_item(20)
#my_list.delete_first()
#my_list.print_list()
#my_list.delete_last()
#my_list.print_list()
#my_list.print_list()       
    
  
    
        








