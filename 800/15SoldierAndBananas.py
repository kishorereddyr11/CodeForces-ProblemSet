k,n,w = map(int,input().split())
ans = ((w*(w+1))//2)*k
ans = max(ans - n, 0)
print(ans)