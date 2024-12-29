text="this is a simple test is a simple"

words=text.split(" ")

wordcount={}

for w in words:

    if w in wordcount:

        wordcount[w]+=1

    else:

        wordcount[w]=1

print(wordcount)

