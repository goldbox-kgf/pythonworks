text="pneumonoultramicroscopicsilicovolcanoconiosis"
v_count=0
c_count=0
vowel_seq=("a","e","i","o","u")
for ch in text:
    if ch in vowel_seq:
        v_count=v_count+1
    else:
        c_count=c_count+1    
print(f"vowel count=",v_count)

print(f"consonent count=",c_count)