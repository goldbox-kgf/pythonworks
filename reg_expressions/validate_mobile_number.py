from re import fullmatch

user_input=input("enter a mobile number:-")

pattern="[0-9]{10}"

matcher=fullmatch(pattern,user_input)

if matcher==None:
    print("invalid")

else:
    print("valid")    