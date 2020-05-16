#Vowels Finder
state_name = [ 'Alabama', 'California', 'Oklahoma', 'Florida']
list1=[]
for state in state_name:
    str1=''
    for word in state:
        if word not in "aeiouAEIOU":
            str1=str1+word
    list1.append(str1)
print(list1)

#version2
list2=list(filter(lambda x:x=='Alabama'  ,state_name))

#verdion3
str3=""
list3=[word for state in state_name  for word in state if word not in "aeiouAEIOU" ]