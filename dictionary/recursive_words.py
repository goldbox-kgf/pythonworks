words=["hello","hai","hello","this","is","this",'is','hello']
word_frequency={w:words.count(w) for w in words}
# print(word_frequency)
recursive_words=[k for k,v in word_frequency.items() if v>1]
print(recursive_words)