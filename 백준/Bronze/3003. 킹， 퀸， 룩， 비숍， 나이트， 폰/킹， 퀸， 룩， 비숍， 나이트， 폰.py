a,b,c,d,e,f = map(int, input().split())
A=[a,b,c,d,e,f]
B=[1,1,2,2,2,8]
box=[]
for i in range(len(A)):
    box.append(-(A[i]-B[i]))
for i in box:
    print(i, end=" ")