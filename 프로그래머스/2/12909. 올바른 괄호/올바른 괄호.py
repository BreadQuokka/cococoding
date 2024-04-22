def solution(s):
    left=0
    right=0
    for i in range(len(s)):
        if s[i] =="(":
            left+=1
        elif s[i]==")":
            right+=1
            if right>left:
                answer=False
                break
    if right==left:
        answer = True
    else:
        answer= False
    
    return answer