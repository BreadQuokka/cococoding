N= int(input())
answer=[]
box=[]
for _ in range(N):
    lst= list(input())
    box.append(lst)

for i in box:#lst=(())())
    left=0
    right=0
    err=[]
    for j in i:

        if j =="(":
            left+=1
        elif j==")":
            right+=1
            if right>left:
                err.append(1)
    
    if len(err) == 0:
        if left== right:
            answer.append("YES")
        else:
            answer.append("NO")
    else:
        answer.append("NO")

    
        
for i in answer:
    print(i)