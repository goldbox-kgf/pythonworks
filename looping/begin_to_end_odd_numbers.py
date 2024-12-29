# begin=int(input("enter the start:"))
# end=int(input("enter the end:"))

# i=begin
# while(i<=end):
#     if i%2!=0:
#         print(i)

#     i=i+1    
# begin=int(input("enter the start:"))
# end=int(input("enter the end:"))


# if begin>end:
#     begin,end=end,begin
# i=begin
# while(i<=end):
#     # if i%2!=0:
#     print(i)

#     i=i+1    

begin=int(input("enter the start:"))
end=int(input("enter the end:"))

reverse= True if begin>end else False
i=begin
while(i<=end if reverse==False else i>=end):
    if i%2==0:
        print(i)
    if reverse==False:
        i=i+1
    else:
        i=i-1

