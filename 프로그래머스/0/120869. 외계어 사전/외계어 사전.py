def solution(spell, dic):
    count=0
    DIC = dic.copy()
    new_dic=[]
    for i in dic:
        if len(spell) != len(i):
            DIC.remove(i)
            
    for i in range(len(DIC)):
        if set(DIC[i])==set(spell):
            count+=1
    if count>=1:
        return 1
    else: 
        return 2
        
    
