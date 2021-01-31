class FindPath:
  def __init__(self, network):
    self.network = network

  def _all_paths(self, network, source, destination, path=[]):
    path = path + [source]
    if source == destination:
      return [path]
    paths = []
    for node in network[source]:
      if node not in path:
        npaths = self._all_paths(network, node, destination, path)
        for npath in npaths:
          paths.append(npath)
    return paths

  def find_path(self, source, destination, type='all'):
    """type: (all, shortest, longest)"""
    paths = self._all_paths(self.network, source, destination)
    if type == 'shortest':
      shortest = None
      for path in paths:
        if not shortest or len(path) < len(shortest):
          shortest = path
      return shortest

    elif type == 'longest':
      longest = None
      for path in paths:
        if not longest or len(path) > len(longest):
          longest = path
      return longest

    else:
      return paths