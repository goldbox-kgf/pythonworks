# start=int(input("enter the start:"))
# end=int(input("enter the end:"))
# seq= range ((int(input("enter start:"),(int(input("enter end:"),(int(input("enter start:")))

# sequence= range((int(input("enter start:"))), (int(input("enter end:"))),(int(input("enter range :"))))



# for num in sequence:
#     print(num)



start=int(input("enter the start:"))
end=int(input("enter the end:"))    

if start<end:
    for num in range(start,end+1,1):
        print(num)

else:
    for num in range(start,end-1,-1):
        print(num)
