# arr=[1,3,4,5]
# n=1
# for i in range(0,len(arr)):
#     if n==arr[i]:
#         n=n+1
#         break

# print(n)


arr=[1,2,4,5]

for i in range(0,len(arr)-1):
    j=i+1
    result=arr[j]-arr[i]
    if result!=1:
        print(arr[i]+1,"missing number")
        break