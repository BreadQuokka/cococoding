l,s = map(int,input().split())
gr1 =set()
gr2 = set()
for i in range(l):
    gr1.add(input())
for i in range(s):
    gr2.add(input())

ans=[]
count=0
for i in gr2:
    if i in gr1:
        count+=1
        ans.append(i)
print(count)
ans.sort()
for i in ans:
    print(i)

