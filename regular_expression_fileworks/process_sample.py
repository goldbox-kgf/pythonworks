# from re import finditer
# f=open("regular_expression_fileworks/sample (1).txt")

# for line in f:
#     web=line.rstrip("\n")

#     pattern="https?://[\w\S./]+"

#     matcher=finditer(pattern,web)
#     for obj in matcher:
#         #   print(obj.group()) 


# ANOTHER METHOD 
from re import findall        
f=open("regular_expression_fileworks/sample (1).txt")
content=f.read()
pattern="https?://[\w\S./]+"
urls=findall(pattern,content)
for url in urls:
    print(url)

    
