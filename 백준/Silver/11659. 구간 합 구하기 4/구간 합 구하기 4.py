n,m= map(int,input().split())
lst = list(map(int,input().split()))
box=[0]
now =0
for i in lst:
    now+=i
    box.append(now)

for i in range(m):
    a,b = map(int,input().split())
    print(box[b]-box[a-1])