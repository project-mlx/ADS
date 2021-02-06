#Queue creation using list
class LinearDS:
  def __init__(self):
    self.ds = []
  
  def insert(self, val): #Enqueue or push at the rear
    self.ds.append(val)
  
  def remove(self, method=None):
    """
    method: (q, s)
    """
    if self.ds:
      if method == 'q': #Dequeue from the front if the method is Queue
        del self.ds[0]
      elif method == 's': #Pop from the rear if the method is Stack
        del self.ds[-1]
      else:
        print('method doesn\'t exist')
    else:
      print('There is nothing in the list to dequeue')
  
  def print_ds(self):
    print(self.ds)

