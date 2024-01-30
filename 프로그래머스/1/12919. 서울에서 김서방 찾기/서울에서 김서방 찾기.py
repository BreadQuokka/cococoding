def solution(seoul):
    count=0
    while seoul:
        if seoul.pop(0)!="Kim":
            count+=1
        else: 
            break
    return f'김서방은 {count}에 있다'
            
