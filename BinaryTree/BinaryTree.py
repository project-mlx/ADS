class Node:
  def __init__(self, element):
    self.root = element
    self.left = None
    self.right = None

  # using recursion to insert values, the function will keep checking 
  #if the data exist on root, left, and right until it assigns the value.
  def insert(self, element):
      if self.root:
        #if element is bigger than the root, it will go to the right node, otherwise, left. 
        if element > self.root: 
          if self.right:
            self.right.insert(element)
          else:
            self.right = Node(element)
        elif element < self.root:
          if self.left:
            self.left.insert(element)
          else:
            self.left = Node(element)
        else:
          self.root = element
      else:
        self.root = element

  def insertList(self, elements): #Function to insert a list of elements
    for element in elements:
      self.insert(element)

  #using recursion here as well, the search will extract from 
  #left (until its over) then to right (until its over) and keep  
  def print_tree(self): 
    if self.root:
      print(self.root)
      if self.left:
        self.left.print_tree()
      else:
        pass
      if self.right:
        self.right.print_tree()
      else:
        return
    else:
      return