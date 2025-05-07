#Convert a tuple to a list and then append items

tuple_items=("apple","banana","cherry")
list_items=list(tuple_items)

while True:
    item=input("Enter an ibtem to append to the list or enter 'done' to end:")
    if item=='done':
        break
    list_items.append(item)
    
updated_tuple=tuple(list_items)
print(updated_tuple)
