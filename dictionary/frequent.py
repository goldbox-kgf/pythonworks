text="ABAABBC"
def get_count(ch):
    return text.count(ch)
most_freq=max(text,key=get_count)    
print(most_freq)