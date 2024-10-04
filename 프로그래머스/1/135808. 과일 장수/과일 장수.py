def solution(k, m, score):
    #m은 세트갯수
    #시점? 
    n=0
    ans=0
    score.sort(reverse=1)
    for i in range(len(score)//m):
        gr=score[n:n+m]
        plus= min(gr)*m
        n+=m
        ans+=plus
        
    return ans