n,k = list(map(int,input().split()))
arr = list(map(int,input().split()))
numk = arr[k-1]
count = 0
for i in range(len(arr)):
    if arr[i]>=numk and arr[i]>0:
        count+=1
print(count)