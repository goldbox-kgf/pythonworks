
f=open("assignment3/qst5.1.txt","r")

string=""

for i in f:

    string+=i

f.close()

f_write=open("assignment3/qst5.2.txt","w")

f_write.write(string)

f_write.close()

