n = int(input())
a=0
b=0
box=[]
for i in range(n):
    a,b = map(int,input().split())
    box.append([a,b])

box.sort(key = lambda x: (x[0],x[1]))
for i in box:
    for j in i:
        print(j, end =" ")
    print()

