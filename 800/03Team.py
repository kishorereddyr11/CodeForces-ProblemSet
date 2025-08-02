n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))
TotalCount = 0
for i in range(n):
    count = 0
    for j in range(3):
        if arr[i][j]==1:
            count+=1
    if count>=2:
        TotalCount+=1
print(TotalCount)

