#Translate Function
str1="This is fun"
def translate(s):
    str2=''
    for letter in s:
        if letter not in "aeiouAEIOU ":
            str2=str2+letter+'o'+letter
        else:    
            str2=str2+letter
    return (str2)       

print(translate(str1))        
