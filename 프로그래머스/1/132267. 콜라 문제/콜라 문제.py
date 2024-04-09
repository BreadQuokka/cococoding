def solution(a, b, n):
    

    count=0
    while n>=a:
        n-=a
        n+=b
        count+=b
        
    return count