#create a tuple using list and string

list=[]

while True:
    item=input("Enter an item to add to the list or enter 'done':")
    if(item=='done'):
        break
    list.append(item)
    
string=input("Enter a string    junjhn :")

tuple_items=tuple(list)+tuple(string)

print(tuple)
