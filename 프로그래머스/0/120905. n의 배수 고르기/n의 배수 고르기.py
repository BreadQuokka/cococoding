def solution(n, numlist):
    new=numlist.copy()
    for i in numlist:
        if i%n !=0:
            new.remove(i)
            
    return new