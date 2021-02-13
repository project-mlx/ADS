class BubbleSort:
  def __init__(self):
    pass
  
  def _check_if_sorted(self, li):
    not_sorted = False
    for i in range(1, len(li)-1):
      if li[i] < li[i-1]:
        not_sorted = True
    return not_sorted

  def sort(self, li):
    while self._check_if_sorted(li):
      for i in range(1, len(li)-1):
        if li[i-1] > li[i]:
          li[i-1], li[i] = li[i], li[i-1]
    return li