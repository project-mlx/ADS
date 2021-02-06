from LinearStackQueue import LinearDS as LDS

ds = LDS()

ds.insert(1)
ds.insert(2)
ds.insert(3)
ds.insert(4)
ds.insert(5)

print('The orginal structure:')
ds.print_ds()

ds.remove(method='q')
print('dequeued using Queue method:')
ds.print_ds()

ds.remove(method='s')
print('popped using Stack method:')
ds.print_ds()
