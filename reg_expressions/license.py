from re import fullmatch
license_num=input("enter number")
pattern="KL[0-9]{2}\s[0-9]{11}"
matcher=fullmatch(pattern,license_num)
if matcher==None:
    print("invalid")
else:
    print("valid")