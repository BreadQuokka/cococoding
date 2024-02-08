def solution(n):
    CNT=0
    for i in range (1,n+1):
        count=0
        for e in range(1,i+1):
            if i%e==0:
                count+=1
        if count>=3:
            CNT+=1
            
    return CNT