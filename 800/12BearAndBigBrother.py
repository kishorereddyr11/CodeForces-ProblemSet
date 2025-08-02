L,B = map(int,input().split())
year = 0
while L<=B:
    L*=3
    B*=2
    year+=1
print(year)