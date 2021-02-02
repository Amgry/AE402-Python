math=input("math percentage")
math=int(math)
english=input("english percentage")
english=int(english)
if(math>=90 and english>=90):
    print("u get prize")
elif(math==100 or english==100):
    print("u still get prize")
else:
    print("ok")