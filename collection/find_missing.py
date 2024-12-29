# arr=[1,3,4,5]
# find missing +ve integer


arr2=[1,2,3,5]
sum_of_list=sum(arr2)
maximum=max(arr2)
total=0
for i in range(1,maximum+1):
    total=total+i

if total==sum_of_list:
    print("least=",maximum+1) 
else:
    print("least=",total-sum_of_list)       