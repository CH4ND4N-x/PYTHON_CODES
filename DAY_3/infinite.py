#Infinite input
small=None
big=None
all_num=[]
while True:
    num=input("Enter a number:").strip()
    if not num:
        break
    num=int(num)
    all_num.append(num)
    if (small is None or num<small):
        small=num
    if (big is None or num>big):
        big=num
print(all_num)
print("Sum of all numbers    :",sum(all_num))
print("Average of all numbers:",sum(all_num)/len(all_num))
print("largest number        :",big)
print("smallest number       :",small)