def solution(n):
    box =[]
    for i in range (1,n+1):
        if n % i ==0:
            box.append(i)
    ans =sum(box)    
    return ans