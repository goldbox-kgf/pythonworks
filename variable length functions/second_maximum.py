def second_max_num(*args):
    sorted_numbers=sorted(args,reverse=True)
    return sorted_numbers[1]

print(second_max_num(11,25,45,68,98,75,28,69,76,89))    