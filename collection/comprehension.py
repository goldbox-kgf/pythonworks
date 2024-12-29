# vowels and consonants 
text=["apple","iphone","orange","potato"]
vowel_words=[w for w in text if w[0]  in ['a','e','i','o','u']]
print (vowel_words)
consonant_words=[w for w in text if w[0] not in ['a','e','i','o','u']]
print(consonant_words)
# longestword
long=max([len(w) for w in text])
longest_words=[w for w in text if len(w)==long]
print(longest_words)