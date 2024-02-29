def solution(strings, n):
    box=[]
    ans=[]
    for i in range(len(strings)):
        box.append(strings[i][n])
        box=sorted(box)
    strings=sorted(strings)
    for i in (box):
        for m in range(len(box)):
            if i==strings[m][n]:
                if strings[m] not in ans:
                    ans.append(strings[m])
                
    
    return ans