num1=int(input("enter the number:"))
num2=int(input("enter the number:"))

largest=max(num1,num2)

for i in range(largest,(num1*num2)+1,largest):
    if i%num1==0 and i%num2==0:
        print(i)

        break