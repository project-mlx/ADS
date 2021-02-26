def insertion_sort(li):
  for i in range(1,len(li)):
    k = li[i]
    n = i-1
    while n >= 0 and k < li[n]:
      li[n+1] = li[n]
      n -= 1
    li[n+1] = k

list_to_sort = [12, 11, 35, 14, 12, 67, 89]

insertion_sort(list_to_sort)

print(list_to_sort)