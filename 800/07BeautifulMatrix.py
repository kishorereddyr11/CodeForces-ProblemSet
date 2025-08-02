arr = [list(map(int,input().split())) for _ in range(5)]
m,n = -1,-1
for i in range(len(arr)):
    for j in range(len(arr[0])):
        if arr[i][j]==1:
            m,n = i,j
print(abs(m-2)+abs(n-2))