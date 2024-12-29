text="ababbccdde"
frequency_count={ch:text.count(ch) for ch in text}
# print(frequency_count)
# for k,v in frequency_count.items():
    # if v==1:
        # print(k)

non_recursive_characters=[k for k,v in frequency_count.items() if v==1]     
print(non_recursive_characters)   