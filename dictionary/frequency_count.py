# arr=[10,20,30,40,50,1,2,10,40,78,10]
# result={num:arr.count(num) for num in arr}
# print(result)

def count_alphabets(string):
    count = 0
    for char in string:
        if char.isalpha():
            count += 1
    return count

print(count_alphabets(""))    