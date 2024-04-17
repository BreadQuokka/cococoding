N= int(input())
box=[]
for _ in range(N):
    a=int(input())
    if a==0:
        box.pop()
    else:
        box.append(a)
print(sum(box))