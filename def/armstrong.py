def if_armstrong(num):

    count=len(str(num))

    original=num

    tot=0

    while(num!=0):

        tot+=(num%10)**count

        num=num//10

    

    print( "is an armstrong no" if original==tot else "is not an armstrong")

if_armstrong(154)