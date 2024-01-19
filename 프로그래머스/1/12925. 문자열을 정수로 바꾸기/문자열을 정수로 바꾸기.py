def solution(s):
    box=[]

    for i in s:
        if i==('+'):
            box.append('+')
        elif i==('-'):
            box.append('-')
        else:
            box.append(i)
    sol=int("".join(box))
        
    return sol