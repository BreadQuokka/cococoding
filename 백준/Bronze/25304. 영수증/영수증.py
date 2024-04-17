price=int(input())
n=int(input())
box=[]
for i in range(n):
    a,b= map(int,input().split())
    total= a*b
    box.append(total)
if sum(box)==price:
    print('Yes')
else:
    print('No')
