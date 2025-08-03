n = int(input())
s = list(input())
if n==1:
    print(0)
    exit()
count = 0
for i in range(1,n):
    if s[i]==s[i-1]:
        count+=1
print(count)