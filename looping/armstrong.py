num=int(input("enter the number:"))

digit_count=len(str(num))

orginal=num

total=0

while(num!=0):
    digit=num%10
    
    exponent=digit**digit_count

    total=total+exponent

    num=num//10

print(f"armstrong {total}" if total==orginal else "{total}not armstrong")
