# Create a list of absentee
fp=open("absentee.txt",'w')
for x in range(25):
    name=input("Enter name:")
    if not name:
        break
    else:
        fp.write(name+'\n')
fp.close() 
list1=[]
fp=open("absentee.txt",'r')
print(fp.readlines())        
fp.close()