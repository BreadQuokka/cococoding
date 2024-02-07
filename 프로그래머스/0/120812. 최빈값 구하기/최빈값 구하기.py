def solution(array):
    S=list(set(array)) # [1,2,3,4]
    box=[]
    for i in S:
        c= array.count(i)
        box.append(c)
        
    if box.count(max(box))>=2:#[1,1,3,1]
        return -1
    else:
        freq_index= box.index(max(box))
        ans= S[freq_index]
        return ans
