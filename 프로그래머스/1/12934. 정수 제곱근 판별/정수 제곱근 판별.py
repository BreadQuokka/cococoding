def solution(n):
    for i in range (1, n+1):
        if n==i**2:
            return (i+1)**2
        
    return -1
    
   