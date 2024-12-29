num1=int(input("enter the number1:="))
num2=int(input("enter the number2:="))

try:
    result=num1/num2
    print(result)

except:
    print("error occured")
    num2=int(input("enter the number2:="))
    result=num1/num2
    print(result)

finally:
    print("file write") 
    print("database committed")
