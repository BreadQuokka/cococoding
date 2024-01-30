def solution(slice, n):
    pizza=1
    cut=slice
    while slice<n:
        pizza+=1
        slice=(pizza*cut)
        
    return pizza