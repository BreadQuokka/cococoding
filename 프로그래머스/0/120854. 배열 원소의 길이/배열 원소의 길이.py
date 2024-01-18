def solution(strlist):
    box=[]
    for i in range (len(strlist)):
        a=len(str(strlist[i]))
        box.append(a)
    return box