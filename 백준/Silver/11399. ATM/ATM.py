n = int(input())
lst = list(map(int, input().split()))
lst.sort()
#12334
ans=0
mid=0
for i in lst:
    mid+=i
    ans+=mid

print(ans)