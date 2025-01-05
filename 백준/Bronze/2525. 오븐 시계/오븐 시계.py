h, m = map(int, input().split())
plus= int(input())

total = m+plus
if h+total//60>=24:
    ans1 = (h+total//60)%24
else:
    ans1=h+total//60
ans2 = total%60

print(ans1,ans2)