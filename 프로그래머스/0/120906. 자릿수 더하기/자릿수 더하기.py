def solution(n):
    a=list(str(n)) #['2','1','3']
    i=1
    box=[]
    for i in range(len(a)):
        box.append(int(a[i-1]))
        
    ans=sum(box)
    return ans
    
    
    
    