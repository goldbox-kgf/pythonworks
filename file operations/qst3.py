
f=open("assignment3/qst3.txt","r")

string=""

for i in f:

    string+=i

word=string.split(" ")

count=0

for w in word:

    count+=1


print(count)

