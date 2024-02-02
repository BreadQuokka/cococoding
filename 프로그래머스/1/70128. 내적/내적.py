def solution(a, b):
    box=[]
    while a:
        A=a.pop(0)
        B=b.pop(0)
        box.append(A*B)
    return sum(box)
    