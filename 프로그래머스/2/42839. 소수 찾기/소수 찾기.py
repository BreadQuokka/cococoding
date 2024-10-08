from itertools import permutations

def yaksu(x):
    if x<2:
        return False
    for i in range(2,int(x**0.5)+1):
        if x%i ==0:
            return False
    return True
    
        
def solution(numbers):
    # 순열인데 len(numbers) 만큼 반복
    # 각 반복 돌면서 소수인지 확인해야 함
    
    a= list(numbers)#[0,1,1] / [1,7] 
    box=[]
    for i in range(1,len(numbers)+1):
        if i != 1:
            for j in permutations(a,i):
                middle = "".join(j)
                if int(middle) not in box:
                    box.append(int(middle))
        else:#if i== 1
            for k in a:
                if int(k) not in box:
                    box.append(int(k))
    

    ans=0
    for k in box:
        if yaksu(k):
            ans+=1
            
    return ans


