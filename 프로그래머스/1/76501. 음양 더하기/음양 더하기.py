def solution(absolutes, signs):
    box=[]
    box1=[]
    while signs:
        if signs.pop()==True:
            box.append(absolutes.pop())
        else:
            box1.append(absolutes.pop())
    plus=sum(box)
    minus=sum(box1)*-1
    return plus+minus