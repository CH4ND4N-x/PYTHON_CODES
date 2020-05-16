#String Handling
Name=input("Enter first and last name:")
x=Name.index(" ")
print(Name[x+1:]+ " "+Name[:x])