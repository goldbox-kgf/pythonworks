expenses=[10000,11000,120000,100,13000]
min_exp=0
for exp in expenses:
    if min_exp<exp:
        max_exp=exp
print(max_exp)
