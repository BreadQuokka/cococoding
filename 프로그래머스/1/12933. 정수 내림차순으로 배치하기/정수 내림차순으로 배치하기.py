def solution(n):
    a= list(str(n))
    b= sorted(a, reverse = 1)
    c= "".join(b)
    return int(c)
