num=int(input("enter the number:"))
total=0
while(num!=0):
    digit=num%10
    
    temp=digit**2

    total=total+temp

    num=num//10

print(total)    