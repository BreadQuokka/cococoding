n,x = map(int,input().split())
ans= map(int,input().split())
ans = list(ans)
box=[]
for i in ans: 
    if i<x:
        box.append(i)
for i in box:
    print(i,end=" ")
    