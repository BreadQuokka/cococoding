n,m = map(int,input().split())
set1=set()
box=[]
count=0
for i in range(n):
    set1.add(input())

for i in range(m):
    box.append(input())

for i in box:
    if i in set1:
        count+=1
print(count)