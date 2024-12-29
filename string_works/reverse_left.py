text="pythonprogramming"
o_index=text.index("o")
reversed_sub=text[o_index-1::-1]
# print(reversed_sub)
balance_sub=text[o_index:]
result=reversed_sub+balance_sub
print(result)

