score=input("score percentage")
score=int(score)
if(score<0 and score>101):
    print("not valid socre")
elif(score>=90 and score<=100):
    print("a")
elif(score>=80 and score<=80):
    print("b")
elif(score>=70 and score<=79):
    print("c")
elif(score>=60 and score<=69):
    print("d")
else:
    print("e")