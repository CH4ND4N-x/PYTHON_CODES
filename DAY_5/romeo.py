# Romeo and Juliet
dict1={}
with open("romeo.txt",'r') as file:
    for line in file:
        for word in line.split():
            word.lower()
            if word in dict1:
                dict1[word]=dict1[word]+1
            else:
                dict1[word]=1
print(dict1)