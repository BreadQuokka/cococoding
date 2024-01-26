def solution(s):
    a=list(s.lower())
    pp= a.count('p')
    yy= a.count('y')
    if (pp==yy) or ((pp==0)&(yy==0)):
        return True
    else:
        return False
    