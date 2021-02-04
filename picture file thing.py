file=open("dog2.jpg","rb")
img=file.read()

file.close()

file=open('dog3.jpg','wb')
file.write(img)
file.close()