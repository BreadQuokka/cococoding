def solution(n):
    import math
    
    a=math.sqrt(n)
    if a == int(a) and a>=1:
        return 1
    else:
        return 2
