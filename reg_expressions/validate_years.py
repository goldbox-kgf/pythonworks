from re import fullmatch
year=input("enter year :")
pattern="(18)[0-9]{2}|(19)[0-9]{2}|(200)[0-9]{1}|(201)[0-9]{1}|(202)[0-4]{1}"
matcher=fullmatch(pattern,year)
if matcher==None:
    print("invalid")
else:
    print("valid")