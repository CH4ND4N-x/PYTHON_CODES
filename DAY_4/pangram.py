#Pangram
str1=input("Enter a sententence:")
def check(data):
    alpha="abcdefghijklmnopqrstuvwxyz"
    for letter in alpha:
        if letter not in data.lower():
            return False
    else:
        return True
if(check(str1)==True):
    print("PANGRAM")
else:
    print("NOT PANGRAM")    
            