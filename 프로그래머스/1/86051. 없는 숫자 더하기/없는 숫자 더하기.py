def solution(numbers):
    new= [1,2,3,4,5,6,7,8,9,0]
    while numbers :
        a= numbers.pop()
        for i in range(10):
            if a == i:
                new.remove(i)
                           
    return sum(new)