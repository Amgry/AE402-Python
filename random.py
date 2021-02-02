import random
x=random.randint(1,10)
no=input("random number from 1 to 10")
no=int(no)
x=int(x)
if(no==x):
    print("u got it right")
elif(x>=11 or x<=0):
    print("i dont think that number is between 1 to 10")
else:
    print("try again")
