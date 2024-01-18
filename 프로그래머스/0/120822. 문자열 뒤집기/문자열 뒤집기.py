def solution(my_string):
    a=list(my_string)
    newlist=[]
    for i in reversed(a):
        newlist.append(i)
    b= "".join(newlist)
        
    return b