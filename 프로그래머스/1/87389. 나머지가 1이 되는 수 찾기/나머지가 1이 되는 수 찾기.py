def solution(n):
    x=1
    while x<=n:
        k=n%x
        x+=1
        if k==1:
            return x-1
            break