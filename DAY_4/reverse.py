#Reverse Function
str1=input("Enter string:")
def reverse(s): 
  str2= "" 
  for i in s: 
    str2= i + str2
  return str2
print("Reverse string:"+reverse(str1))