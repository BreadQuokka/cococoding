from itertools import combinations

box=[]

def solution(number):
    
    comb = combinations(number,3)
    a=(list(comb))
    
    for i in a:
        if sum(i)==0:
            box.append(i)
    
    return len(box)