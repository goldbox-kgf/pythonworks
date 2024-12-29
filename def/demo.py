def sum(num1,num2):
    result=num1+num2

    print(result)
# sum(100,200)

def mul(num1,num2):
    result=num1*num2
    print(result)
# mul(5,5)    

def div(num1,num2):
    result=num1/num2
    print(result)
# div(115,2)    

def last_digit(num1,num2):
    num1_last_digit=num1%10
    num2_last_digit=num2%10
    print(num1 if num1_last_digit>num2_last_digit else num2)
last_digit(123,871)    