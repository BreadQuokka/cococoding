def solution(n):
    box=[]
    count=0
    while len(box)<n:
        if count%2==0:
            box.append('수')
            count+=1
        else:
            box.append("박")
            count+=1
    return "".join(box)