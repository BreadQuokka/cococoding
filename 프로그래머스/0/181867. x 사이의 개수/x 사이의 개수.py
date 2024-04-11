def solution(myString):
    box=[]
    answer = myString.split("x")
    for i in answer:
        box.append(len(i))
        
    return box