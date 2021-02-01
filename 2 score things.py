math=input("math percentage")
math=int(math)
english=input("english percentage")
english=int(english)
if(math>=90 and english>=90):
    print("u get a prize")
elif(math>=90 and english<60)or(math<60 and english>=90):
    print("try harder next time")
elif(math<60 and english<60):
    print("u failed")
else:
    print:("ok")