n=int(input("How many grade do you have"))
score=[]
name=[]
highest=0
lowest=100
lowestname=""
highestname=""
summath=0
for i in range(n):
   mathname=(input("name?"))
   mathscore=int(input("math score"))
   name.append(mathname)
   score.append(mathscore)
   if highest<mathscore:
           highest=mathscore
           highestname=mathname
           summath=summath+mathscore
   if lowest>mathscore:
        lowest=mathscore
        lowestname=mathname
        print(highest,highestname)
        print(lowest,lowestname)
        print("avg", summath/n)
        