def solution(my_string):
    box=[]
    for i in range(len(my_string)):
        box.append(my_string[i:])
        box=sorted(box)
    return box