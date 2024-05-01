from itertools import permutations
def solution(numbers):
    # box1=[]
    # for i in numbers:
    #     box1.append(str(i))#['6','10','2']
    # a=permutations(box1,len(numbers))
    # lst= list(a)
    # box=[]
    # for i in lst:
    #     ans=""
    #     for j  in i:
    #         ans+=j
    #     box.append(ans)
    box=[]
    flag = True
    for i in numbers:
        if i != 0:
            flag = False
        box.append(str(i)*3)
    if flag == True:
        return "0"
    a= sorted(box, reverse=True)
    ans=""
#     for i in range(len(a)-1):
#         if len(a[i])!=1 & len(a[i+1])==1:
#             a[i],a[i+1]= a[i+1],a[i]
#     # 합치기
#     for i in a:
#         ans+=i

   
    for i in a:    
        b=i[:int(len(i)/3)]# a[0] 은 666
        ans+=b
    return ans


    