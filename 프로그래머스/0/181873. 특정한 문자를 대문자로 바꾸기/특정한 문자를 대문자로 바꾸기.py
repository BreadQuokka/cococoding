def solution(my_string, alp):
    ans=""
    for i in my_string:
        if i == alp:
            a=i.upper()
        else:
            a=i
        ans+=a
    return ans