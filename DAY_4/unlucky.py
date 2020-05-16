#Unlucky 13
numbers= input("Enter comma seperated numbers >").split(",")

previous = False
total = 0

for number in numbers:
    if int(number) == 13:
        previous= True
    
    elif not previous:
        total = total+ int(number)
    
    elif previous and int(number) != 13:
        previous = False

print (total)