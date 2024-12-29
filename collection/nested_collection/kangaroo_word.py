source_word=input("enter the source word:-")
target_word=input("enter the target word:-")
# character_count={}
# for ch in source_word:
#     if ch in character_count:
#         character_count[ch]+=1
#     else:
#         character_count[ch]=1

character_count={ch:source_word.count(ch) for ch in source_word}    
# print(character_count)
is_kangaroo=True
for ch in target_word:
    if ch in character_count and character_count.get(ch)>0:
        character_count[ch]-=1
    else:
        is_kangaroo=False
        break

print(is_kangaroo)    
