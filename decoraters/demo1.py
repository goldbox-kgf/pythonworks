def round_decorator(fn):
    def wrapper(n1,n2):
        n1=round(n1)
        n2=round(n2)   
        return fn(n1,n2)
    return wrapper 


def swap_decorator(fn):
    def wrapper(n1,n2):
        if n1<n2:
            (n1,n2)=(n2,n1)
        return fn(n1,n2)
    return wrapper 
@round_decorator
@swap_decorator
def add_number(num1,num2):
    return num1+num2
@round_decorator
@swap_decorator
def sub_number(num1,num2):
    return num1-num2
@round_decorator
@swap_decorator
def div_number(num1,num2):
    return num1/num2


print(div_number(3.7,27.2))    
print(sub_number(333,27))    
print(add_number(35.6,27.2))    
print(add_number(-3,27))    