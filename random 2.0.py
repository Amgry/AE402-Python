import random
t=0
while t<=5:
    x=random.randint(1,20)
    no=input("random number from 1 to 20")
    no=int(no)
    x=int(x)
    if(no==x):
        print("u got it right",count)
        t=t+6
    elif(x<no):
        print("too big")
    elif(x>no):
        t=t+1
        print("too small")
        t=t+1
    elif(t==5):
        print("u lose",x)
        