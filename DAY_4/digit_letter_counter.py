#Digit Letter Counter
import string
a=0
b=0
str1=(input("Enter :"))
for letter in str1:
    if letter in string.ascii_letters:
        a=a+1
    elif letter in string.digits:
        b=b+1
print("letter:",a,"digit:",b) 