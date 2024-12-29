text="On June 5th, 2024 ,we will celebrate @ our annual event: 'Tech innovations 2024!'"

#alphabet count
def count_alphabets(string):
    count = 0
    for char in string:
        if char.isalpha():
            count += 1
    return count

# print(count_alphabets("On June 5th, 2024 ,we will celebrate @ our annual event: 'Tech innovations 2024!'")) 

#no.of spaces
spaces = text.count(' ')
# print("Number of spaces:", spaces)


# no of special characters
def count_special_characters(string):
    special_char_count = 0
    for char in string:
        if not char.isalnum():  
            special_char_count += 1
    return special_char_count

# print(count_special_characters("On June 5th, 2024 ,we will celebrate @ our annual event: 'Tech innovations 2024!'"))   

# count of numbers




text="On June 5th, 2024 ,we will celebrate @ our annual event: 'Tech innovations 2024!'"

count = 0
def count_numbers(string):
    for ch in string:
        if ch.isnumeric():
         count+=1

print("The number count:",count)
