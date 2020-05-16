#Supermarket
dict1={}
while True:
    item_name=input("Enter item name:")
    if not item_name:
        break
    quantity=int(input("Enter the quantity:"))
    if item_name not in dict1:
        dict1[item_name]=quantity
    else:
        dict1[item_name]=dict1[item_name]+quantity
        
for key, values in dict1.items():
    print(key, values)        