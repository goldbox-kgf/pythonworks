input=input("enter the string")

f=open("assignment3/qst2.txt","a")

words=input.split(" ")

for i in words:

    f.write(i+"\n")

f.close()