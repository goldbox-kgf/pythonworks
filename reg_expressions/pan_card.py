from re import fullmatch
pan_cardno=input("enter pan cardnumber :")
pattern="[A-Z]{3}[PCAFHT][A-Z]{1}[0-9]{4}[A-Z]{1}"
matcher=fullmatch(pattern,pan_cardno)
if matcher==None:
    print("invalid")
else:
    print("valid")