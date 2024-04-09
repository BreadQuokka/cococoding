def dev(x):
    box=[]
    for i in range(1,x+1):
        if x%i ==0:
            box.append(i)
    return len(box)

def solution(left, right):
    ans=0
    for j in range(left,right+1):#13
        if dev(j)%2==0:
            ans+=j
        else:
            ans-=j
        
            
    return ans