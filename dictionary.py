d={}
t=False
print("---------")
print("hallo")
print("---------")
while t=True:
    print("=>")
    print("1.add word")
    print("2.list words")
    print("3.translate english to chinese")
    print("4.translate chinese to  english")
    print('5."fun" game')
    print("6.leave")
    sel=input("enter option")
    if sel=='1':
        while True:
            voc=input("add word(press 0 to leave)")
            if (voc=='0'):
                break
            if (voc not in d):
                m=input("enter word")
                d[voc]=m
            else:
                print("word already exists")
    elif sel=='2':
        lk=sorted(d)
        for item in lk:
            print(item,'is',d[item])
    elif sel=='3':
       voc=input('word to translate')
       if voc=='0':
           break
       if voc in d:
           print(d[voc])
       else:
           print('we dont have this word')
    elif sel=='4':
        got=False
        voc=input("enter word to translate")
        if voc=='0':
            break
        if voc in d:
            print(d[voc])
        else:
            print("we dont have this word")
        if ch=='0':
            break
        for k,v in d.items():
            if ch==v:
                print(ch,'in english is',k)
                got=True
            if not got:
                print("sorry,we dont have that word")
    elif sel=='5':
        score=0
        print("the total score is",len(d),'points')
        for k,v in d.items():
            print(v,":")
            ans=input()
            if ans==k:
                score+=1
                print("correct")
    elif (sel=='6'):
        break
    else:
                print("entered wrong, please eneter new one")
                print("wrong")