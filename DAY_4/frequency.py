#Character Frequency
dict1={}
str1=input("Enter a string:")
for letter in str1:
    if letter not in dict1:
        dict1[letter]=1
    else:
        dict1[letter]=dict1[letter]+1
for key, value in dict1.items():
    print(key, value)        