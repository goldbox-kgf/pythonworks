arr=[100,200,300,400,500]
k=2
# rotate araay k times
for i in range(1,k+1):
    popped=arr.pop()
    arr.insert(0,popped)

print(arr)    