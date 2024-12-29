input=input("enter the string")

f=open("assignment3/qst1.txt","w")

for i in input:

    f.write(i)

f.close()

f1=open("assignment3/qst1.txt","r")

for word in f1:

    print(word)

f1.close()

