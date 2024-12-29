text="The quick brown fox umps over the lazydog".casefold()
# text2=text.casefold
pangram_seq=("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")
for ch in text:
    if ch in pangram_seq:
       
       print("pangram")
       break

    else:
    
      print("not pangram")   

