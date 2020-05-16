#Letter Distribution
import string
total_count=0
str1 = input("Enter a string: ").lower()
dict1={}
for letter in str1:
    if letter not in dict1:
        dict1[letter]=1
    else:
        dict1[letter]=dict1[letter]+1
        
total_count = sum(list(dict1.values()))
for letter, count in dict1.items():
    print(f"{letter}: {count} {int(count/total_count*100)}%")