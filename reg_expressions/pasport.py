from re import fullmatch
pasport_num=input("enter number")
pattern="[A-Z]{1}\s[0-9]{7}"
matcher=fullmatch(pattern,pasport_num)
if matcher==None:
    print("invalid")
else:
    print("valid")