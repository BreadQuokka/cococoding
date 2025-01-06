def solution(nums):
        
    a=list(set(nums))# [3,2,4]
    if len(a) >= len(nums)//2:
        ans= len(nums)//2
    else:
        ans= len(a)
    return ans