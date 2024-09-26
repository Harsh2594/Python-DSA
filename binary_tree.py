#Implement binary search tree:
class Node:
  def __init__(self,data=None,right=None,left=None):
    self.data = data
    self.right = right
    self.left = left

class BST:
  def __init__(self):
    self.root = None
    self.item_count = 0
  def insert(self,data):
    if self.root is None:
      self.root = Node(data)
    else:
      self._insert(self.root,data)

  def _insert(self,current_node,data):
    if data < current_node.data:
      if current_node.left is None:
        current_node.left = Node(data)
      else:
        self._insert(current_node.left,data)  
    elif data > current_node.data:
      if current_node.right is None:
        current_node.right = Node(data)
      else:
        self._insert(current_node.right,data)        
    else:
      print(f"value {data} already exits in tree")

  def search(self,node,data):
    if node is None:
      return None
    elif node.data == data:
      return node
    elif data > node.data:
      return self.search(node.right,data)
    else:
      return self.search(node.left,data)

#inorder---left->root->right
  def inorder(self,node):
    if node is not None:
      self.inorder(node.left)
      print(node.data,end="->")
      self.item_count += 1
      self.inorder(node.right)
  
#preorder---root->left->right  
  def preorder(self,node):
    if node is not None:
      print(node.data,end="->")
      self.preorder(node.left)
      self.preorder(node.right)

#postorder---left->right->root  
  def postorder(self,node):
    if node is not None:
      self.preorder(node.left)
      self.preorder(node.right)
      print(node.data,end="->")
      
  def minimum_value(self,node):
    if node.left is None:
      return node.data
    else:
      return self.minimum_value(node.left)

  def maximum_value(self,node):
    if node.right is None:
      return node.data
    else:
      return self.maximum_value(node.right)
  
  def delete(self,data):
    self.root = self.rdelete(self.root,data)
  def rdelete(self,node,data):
    if node is None:
      return None
    elif data > node.data:
      node.right = self.rdelete(node.right,data)
    elif data < node.data:
      node.left =  self.rdelete(node.left,data)
    else:
      if node.left is None:
        return node.right
      elif node.right is None:
        return node.left
      node.data = self.minimum_value(node.right)
      self.rdelete(node.right,node.data)
    return node
      
  def size(self):
    return self.item_count
    











bst = BST()
bst.insert(70)
bst.insert(10)
bst.insert(25)
bst.insert(90)
bst.insert(60)
bst.insert(40)
bst.insert(100)
bst.insert(45)       
print(bst.search(bst.root,60).data)
bst.inorder(bst.root)
print()
bst.preorder(bst.root)
print()
bst.postorder(bst.root)
print()
print(bst.minimum_value(bst.root))
print()
print(bst.maximum_value(bst.root))
print(f"Number of item in tree {bst.size()}")