def solution(num, k):
    a=str(num)
    b=str(k)
    if b in a:
        c= a.find(b)
    else: 
        c=-2
    return c+1
        

