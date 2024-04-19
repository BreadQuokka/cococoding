def solution(t, p):
    long=len(p)
    box=[]
    rep= len(p)
    for i in range(len(t)-rep+1):
        str=""
        for j in range (rep):
            str+=t[i+j]
        box.append(str)
        
        
    ans=0
    for i in box:
        if int(i)<=int(p):
            ans+=1
    return ans