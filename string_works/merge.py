# text1="ABCDEF"
# text2="PQRS"
# new=""
# length1=len(text1)
# length2=len(text2)
# for i in range(0,length2):

#     new+=text1[i]+text2[i]
# for j in range(length2,length1):
#     new+=text1[j]

# print(new)

# 2nd method

text1="ABCDEF"
text2="PQRS"
result=""
smallest_text=text1 if len(text1)<len(text2) else text2
largest_text=text1 if text1>text2 else text2
for i in range(0,len(smallest_text)):
    result+=text1[i]+text2[i]

blance_text=""
blance_text+=largest_text[len(smallest_text):]
result+=blance_text
print(result)    