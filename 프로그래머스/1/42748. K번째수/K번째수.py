def solution(array, commands):
    box=[]
    for i in range (len(commands)):
        answer=array[commands[i][0]-1:commands[i][1]]
        answer=sorted(answer)
        a = answer[commands[i][2]-1]
        box.append(a)
    return box

