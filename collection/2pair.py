arr=[2,3,4,5]
sum=int(input("enter sum"))
left=0
right=len(arr)-1
while(left<right):
    current_sum=arr[left]+arr[right]
    if current_sum==sum:
        print(arr[left],arr[right])
       # break
    elif current_sum>sum:
        right=right-1
    elif current_sum<sum:
        left=left+1