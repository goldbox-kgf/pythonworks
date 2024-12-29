from re import fullmatch

gmail_id=input("enter a gmail id :-")

pattern="[a-z]+[a-z0-9]{5,63}@gmail.com"

matcher=fullmatch(pattern,gmail_id)

if matcher==None:
    print("invalid")

else:
    print("valid")    