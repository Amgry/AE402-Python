import random
t=0
while t>=5:
    x=random.randint(1,20)
    no=input("random number from 1 to 20")
    no=int(no)
    x=int(x)
    if(no==x):
        print("u got it right",x)
        t=t+6
    elif(x!=no):
        print("try again")
        t=t+1
    else:
        print("u lose",x)
