# words=["hai","hello","hello","hai"]
# word_count={}
# for w in words:
#     if w in word_count:
#         word_count[w]+=1
#     else:
#         word_count[w]=1
# print(word_count)            

# word count 2

text="REALMADRID"
# ch_count={}
# for ch in text:
#     if ch in ch_count:
#         ch_count[ch]+=1
#     else:
#         ch_count[ch]=1
# print(ch_count)            

# simplest
frequency_count={ch:text.count(ch) for ch in text}
print(frequency_count)