n = int(input())
num = 0
while n>0:
    s = input()
    if s == 'X++' or s == '++X':
        num += 1
    else:
        num -= 1
    n-=1
print(num)