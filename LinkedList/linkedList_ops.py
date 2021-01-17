from LinkedList import LinkedList

LList = LinkedList()
LList.insert(3)
print('\nInserted the first value:')
LList.print_list()

LList.insert(4,pos='start')
print('\nInserted 4 at the start:')
LList.print_list()

LList.insert(5,pos=1)
print('\nInserted 5 on the second index:')
LList.print_list()

LList.insert(6,pos=0)
print('\nInserted 6 on the first index:')
LList.print_list()

print('\nDeleted the last node:')
LList.pop()

print('\nDeleted the first node:')
LList.pop(0)

print('\nDeleted the node on 3rd index:')
LList.pop(2)