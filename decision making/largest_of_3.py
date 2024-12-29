num1=int(input("enter 1st no:"))

num2=int(input("enter 2nd no:"))

num3=int(input("enter 3rd no:"))

if num1==num2 and num2==num3:
    print("numbers are equal")

elif num1>num2:

    print(f"{num1} is greater")

elif num1>num3:

     print(f"{num1} is greater")

elif num2>num3:

    print(f"{num2} is greater")

else:

    print(f"{num3} is greater")