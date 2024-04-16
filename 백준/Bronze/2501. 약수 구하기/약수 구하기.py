N,K= map(int, input().split())
devine=[]
for i in range(1,N+1):
    if N%i==0:
        devine.append(i)
if len(devine)>=K:
    devine=sorted(devine)
    print(devine[K-1])
else:
    print(0)