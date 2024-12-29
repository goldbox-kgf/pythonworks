from re import fullmatch,finditer
f=open("C:\\Users\\Personal\\OneDrive\\Desktop\\pythonprgms\\regular_expression_fileworks\\social_posts.txt")
for line in f:
    
    words=line.rstrip("\n")
    
    pattern="#[a-z]*"

    matcher=finditer(pattern,words)
    for obj in matcher:
          print(obj.group()) 
