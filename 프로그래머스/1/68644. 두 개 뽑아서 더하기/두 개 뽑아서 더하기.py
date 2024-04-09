def solution(numbers):
    box=[]
    for i in range(len(numbers)):#0,1,2,3,4
        a=numbers[i]
        for j in numbers[i+1:]:
            ans= a+j
            box.append(ans)
            
    box.sort()
    box=list(set(box))
    box.sort()
    return box
 

