def solution(numbers, k):
    
    ans=2*k%len(numbers)-2
    return numbers[ans]