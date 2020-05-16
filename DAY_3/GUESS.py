#number GUESS
import random
x=int(random.uniform(0, 11))
limit=0
print("you Only get five chance to guess a number , be wise and smart")
while limit<6:
    print("no of chances",6-limit)
    y=int(input("Guess a number b/w[1-10]:"))
    if x==y:
        print("You WIN")
        ans=input("Want to play again[Y/N]:")
        if (ans=="Y" or ans=="y"):
            limit=-1
        else: break    
    else:
        print("You LOOSE")
    limit=limit+1    