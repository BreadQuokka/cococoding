def solution(num_list):
    box2=[]
    box1=[]
    while num_list:
        a=num_list.pop()
        if a%2==0:
            box2.append(a)
        else:
            box1.append(a)
    a=len(box2)
    b=len(box1)
    ans=[a,b]
    return ans