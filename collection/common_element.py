# first method
# arr=[10,8,69,20,30]
# arr2=[56,78,10,44,8]
# for i in range(0,len(arr)):
#     for j in range(0,len(arr2)):
#         if arr[i]==arr2[j]:
#              print(arr[i])

# second method

arr=[10,8,69,20,30,100]
arr2=[56,78,10,44,8,20]
arr.sort()
arr2.sort()
p1=0
p2=0

while (p1<=len(arr)-1 and p2<=len(arr2)-1):
    if arr[p1]==arr2[p2]:
        print(arr[p1])
        p1+=1
        p2+=1
    elif arr[p1]<arr2[p2]:
        p1+=1

    elif arr[p1]<arr2[p2]:
        p2+=1        