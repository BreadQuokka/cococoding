def solution(a, b):
    A= list(str(a))
    A.append(str(b))
    A="".join(A)
    A=int(A)
    B= 2*a*b
    if A>B:
        return A
    elif A<B:
        return B
    else: 
        return A