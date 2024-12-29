f=open("C:\\Users\\Personal\\OneDrive\\Desktop\\pythonprgms\\file data sets\\question.txt","r")
words=[]
for line in f:
    line=line.rstrip("\n")
    all_words=line.split(" ")
    for w in all_words:
        words.append(w)
print(words)    

word_count={w:words.count(w) for w in words}

value_key=[[v,k] for k,v in word_count.items()]

print(sorted(value_key,reverse=True))