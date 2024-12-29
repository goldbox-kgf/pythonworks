from re import fullmatch
aadhar_num=input("enter number")
pattern="[0-9]{4}\s[0-9]{4}\s[0-9]{4}"
matcher=fullmatch(pattern,aadhar_num)
if matcher==None:
    print("invalid")
else:
    print("valid")