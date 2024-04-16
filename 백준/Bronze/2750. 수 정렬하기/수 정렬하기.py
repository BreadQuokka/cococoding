N=int(input())
box=[]
for i in range(N):
    a=int(input())
    box.append(a)
box.sort()
for i in box:
    print(i)
