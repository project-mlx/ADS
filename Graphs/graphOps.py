from Graphs import FindPath 

#Keys are nodes and the values are the list of nodes 
#that are directly connected to the key node
Network = {
    'Mumbai':['Pune','Goa'],
    'Pune':['Mumbai','Goa','Indore','Gujrat'],
    'Gujrat':['Pune','Indore','Bangalore'],
    'Indore':['Pune','Gujrat','Goa','Bangalore'],
    'Goa':['Mumbai','Pune','Indore','Bangalore'],
    'Bangalore':['Gujrat','Indore','Goa']
}

findPath = FindPath(Network)
source = 'Mumbai'
destination = 'Bangalore'
kind = 'shortest'
paths = findPath.find_path(source, destination, kind)
print('paths from {} to {}: {}'.format(source,destination,paths))