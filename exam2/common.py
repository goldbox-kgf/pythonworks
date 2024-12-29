def most_frequent_word(text: str) -> str:

    words = re.findall(r'\b\w+\b', text.lower())
    
    
    word_count = Counter(words)
    
 
    most_common_word = word_count.most_common(1)[0][0]
    
    return most_common_word
most_frequent_word("all is going is very is well")    