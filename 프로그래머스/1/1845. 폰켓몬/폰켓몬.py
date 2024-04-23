from itertools import combinations
def solution(nums):
#     box=[]
#     long= len(nums)
#     a = list(combinations(nums,long//2))
#     for i in a:
#         if i not in box:
#             box.append(i)
#     box2=[]        
#     for i in box:
#         b= list(set(i))
#         box2.append(len(b))
        
    a=list(set(nums))
    if len(a) >= len(nums)//2:
        ans= len(nums)//2
    else:
        ans= len(a)
    return ans