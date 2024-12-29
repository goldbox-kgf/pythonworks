start=int(input("enter the start number:"))
end=int(input("enter the end number:"))

for num in range(start,end+1):

    is_prime=True

    for i in range(2,num):
        if num%i==0:
            is_prime=False
            break

    if is_prime==True:
        print(num)