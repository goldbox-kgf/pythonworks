num1=int(input("enter 1st no"))

num2=int(input("enter 2nd no"))

num3=int(input("enter 3rd no"))

if num1>num2 and num1<num3:
    if num2>num3:

        print(f"{num2} is 2nd largest")

    else:
        print(f"{num3} is 2nd largest")

elif num2>num1 and num2>num3:
    if num1>num3:
        print(f"{num1} is 2nd largest")

    else:
        print(f"{num3} is 2nd largest")

elif num3>num1 and num3>num2:
    if num1>num2:
        print(f"{num1} is 2nd largest")

    else:
        print(f"{num2} is 2nd largest")    

elif num1==num2==num3:
    print("numbers are equal")        
