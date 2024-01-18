def solution(my_string):
    a=list(my_string)
    newlist=[]
    for i in reversed(a): ##reverse 함
        newlist.append(i)
    b= "".join(newlist)
        
    return b


#혹은
def solution(my_string):
    a=list(my_string)
    newlist=[]
    while a:
        newlist.append(a.pop())
        print(a)
    b= "".join(newlist)
        
    return b

solution("zoooooo")
