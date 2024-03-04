def solution(s):
    box1=[]
    box2=[]
    for i in range(len(s)):
        box1.append(max(s[i]))
        box2.append(min(s[i]))
    a=max(box1)
    b=max(box2)
    return a*b


