def solution(a, d, included):
    cnt = 0
    box = []
    for i in included:
        if i == True:
            box.append(cnt)
        cnt += 1
    #box 0,3,4
    ans=0
    for i in box:
        A=0
        A= a+d*i
        ans+=A
        #0,3,4
        #3, 18, 19
    return ans
        
   

