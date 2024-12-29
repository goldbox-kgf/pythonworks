arr=[2,3,4,5]
sum=8
for i in range(0,2):
    for j in range(i+1,len(arr)):
        current_sum=arr[i]+arr[j]
        if current_sum==sum:

            print(arr[i],arr[j])
            break