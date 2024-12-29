# sub
sub=lambda num1,num2:num1-num2
# print(sub(2,10))

# cube
cube=lambda num:num**3
# print(cube(5))

# add
add=lambda num1,num2:num1+num2
# print(add(4,5))

max_two=lambda str1,str2:str1 if len(str1)>len(str2) else str2
# print(max_two("apple","watermelon"))

smart_sub=lambda num1,num2:num1-num2 if num1>num2 else num2-num1
# print(smart_sub(10,12))

words=["hai","hello","morning","happy","trip"]
get_length=lambda word:len(word)
# print(max(words,key=get_length))

text="this is a simple programming question to find out word with maximum length"
words=text.split(" ")
get_length=lambda word:len(word)
# print(max(words,key=get_length))

text="this is a simple programming question to find out word with maximum length"
words=text.split(" ")
def get_length(w):
    return len(w)
sorted_words=sorted(words,key=get_length,reverse=True)    
# print(sorted_words)

text="this is a simple programming question to find out word with maximum length"
words=text.split(" ")
def get_count(w):
    return words.count(w)

frequent_word=max(words,key=get_count)
# print(frequent_word)