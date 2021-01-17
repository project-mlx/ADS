#Node class for storing data list element 
#and a key (next) for the next node of data
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

#Linked List class for creating the consolidated list and 
#the basic listoperations
class LinkedList:
  def __init__(self):
    self.head = None

      
  #Print the list
  def print_list(self):
    node = self.head
    while node:
      print(node.data)
      node = node.next

  def insert(self, data, pos='end'):
    """
    data: the value you want to insert
    pos: position on which you want your value to be, 
         it can be 'start', 'end', and any number from 0 to N
    """
    #Create a node from data value
    new_node = Node(data)

    #If the head is None set the value on head and end the operation
    if self.head is None:
      self.head = new_node
      return

    #Insert the value at the end of the list (on the tail)
    if pos=='end':
      current = self.head
      while current.next:
        current = current.next
      current.next = new_node

    #Insert the value at the start of the list (on the head)
    elif (pos=='start') | (pos==0):
      new_node.next = self.head
      self.head = new_node

    #Insert the value on the mentioned postion (by number)
    else:
      prev_node = self.head
      while pos is not 1:
        prev_node = prev_node.next
        if prev_node.next == None:
          break
        pos-=1
      new_node.next = prev_node.next
      prev_node.next = new_node

  def pop(self, index=None):  
    
    if self.head is None:
      return 'There is nothing to delete!!'

    #If index is none then delete node of the last index
    if index is None:
      current = self.head
      while current.next:
        if current.next.next is None:
          break
        current = current.next
      current.next = None

      return self.print_list()

    #If index is 0 then delete the first node
    elif index==0:
      self.head = self.head.next
      return self.print_list()

    #Delete the node on the mentioned index
    else:
      current = self.head
      while index is not 1:
        if current.next.next is None:
          break
        current = current.next
        index-=1
      current.next = current.next.next
      return self.print_list()
