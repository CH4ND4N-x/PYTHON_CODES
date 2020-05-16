#Duplicate
list1=[12,24,35,24,88,120,155,88,120,155]
list1.sort()
list1=list(dict.fromkeys(list1))
print(list1)