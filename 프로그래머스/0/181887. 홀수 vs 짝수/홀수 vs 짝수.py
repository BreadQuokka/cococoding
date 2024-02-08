def solution(N):
    box=[]
    box2=[]
    for i in range(len(N)):
        if i%2==1:
            box.append(N[i])
    for i in range(len(N)):
        if i%2==0:
            box2.append(N[i])
    A=sum(box)
    B=sum(box2)
    if A>B:
        return A
    elif B>A:
        return B
    else: return A
        
    
    return sum(box)