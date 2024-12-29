f=open("C:\\Users\\Personal\\OneDrive\\Desktop\\pythonprgms\\file data sets\\fruits.txt","r")
fruits=[]
for line in f:
    fruits.append(line.rstrip("\n"))
print(fruits)