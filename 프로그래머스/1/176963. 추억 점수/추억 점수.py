def solution(name, yearning, photo):
    dic={}
    box=[]
    for i in range(len(name)):
        dic[name[i]]= yearning[i]
    for i in photo:#["may", "kein", "kain", "radi"]
        ans=0
        for j in i:
            if j in dic:
                ans+=dic[j]
        box.append(ans)
            
        
    return box