list=[]
while True:
    
    items=input("Enter the list items:")
    if items=='done':
        break
    list.append(items)
    
strings=input("Enter the string:")
tupleitems=tuple(list)+tuple(strings)
print(tupleitems)
