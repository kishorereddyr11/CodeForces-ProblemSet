n = int(input())
if n<=5:
    print(1)
    exit()
count = 0
while n!=0:
    if n>=5:
        n = n-5
        count+=1
    elif n==4:
        n = n-4
        count+=1
    elif n==3:
        n = n-3
        count+=1
    elif n==2:
        n = n-2
        count+=1
    else:
        n = n-1
        count+=1
print(count)
