def solution(myString):
    idx=['m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    ans=""
    for i in myString:
        if i not in idx:
            ans+="l"
        else:
            ans+=i
    return ans