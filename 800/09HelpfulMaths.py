s = input().split('+')
s.sort()
ans = ""
ans+=s[0]
for i in range(1,len(s)):
    ans+=('+'+s[i])
print(ans)