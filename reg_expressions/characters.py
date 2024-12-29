from re import finditer

text=" I have 3 cars,2 bike and 1 cycle"

# pattern="\w" #check for all lowercase alphabets

# pattern="\d" #check for digits 

# pattern="\D" #for excluding digits

pattern="\W" #special characters[a-zA-Z0-9] 

pattern="\s" #space

pattern="\S" #exclude space 

matcher=finditer(pattern,text)

for obj in matcher:
    print(obj.start(),obj.group())