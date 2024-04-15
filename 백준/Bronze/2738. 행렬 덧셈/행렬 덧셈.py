A,B= map(int,input().split())
#A*B A가 행
a=[]
b=[]
for  i in range(A):
    i= list(map(int, input().split()))
    a.append(i) # [[1,1,1][2,2,2][0,1,0]]
            
for  i in range(A):
    i= list(map(int, input().split()))
    b.append(i)    
            
box=[]
for i in range(A):
    for j in range(B):
        print(a[i][j]+b[i][j],end=" ")
    print()
