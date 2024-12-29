# from re import findall
# f=open("C:\\Users\\Personal\\OneDrive\\Desktop\\pythonprgms\\regular_expression_fileworks\\sample_text.txt")
# for line in f:
#     date=line.rstrip("\n")
#     pattern="[0-9]{2}/[0-9]{2}/[0-9]{4}"
#     matcher=findall(pattern,date)
#     for obj in matcher:
#         print(obj)



# ANOTHER METHOD
from re import findall        
f=open("C:\\Users\\Personal\\OneDrive\\Desktop\\pythonprgms\\regular_expression_fileworks\\sample_text.txt")
content=f.read()
pattern="[0-9]{2}/[0-9]{2}/[0-9]{4}"
dates=findall(pattern,content)
for date in dates:
    print(date)
