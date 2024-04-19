box1= [1, 2, 3, 4, 5]
box2=[2, 1, 2, 3, 2, 4, 2, 5]
box3=[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
 
def solution(answers):
    cnt1=0
    cnt2=0
    cnt3=0
    for i in range(len(answers)):
        if len(answers)<= len(box1):
            if answers[i]==box1[i]:
                cnt1+=1 
        else:
            repeat= len(answers)//len(box1) # 몫
            dum=len(answers)%len(box1) # 나머지
            new_box= box1*repeat+box1[:dum]
            if answers[i]==new_box[i]:
                cnt1+=1  
            
        if len(answers)<= len(box2):
            if answers[i]==box2[i]:
                cnt2+=1
        else:
            repeat= len(answers)//len(box2) # 몫
            dum=len(answers)%len(box2) # 나머지
            new_box= box2*repeat+box2[:dum]
            if answers[i]==new_box[i]:
                cnt2+=1 
        if len(answers)<= len(box3):
            if answers[i]==box3[i]:
                cnt3+=1
        else:
            repeat= len(answers)//len(box3) # 몫
            dum=len(answers)%len(box3) # 나머지
            new_box= box3*repeat+box3[:dum]
            
            if answers[i]==new_box[i]:
                cnt3+=1 
        lst= [cnt1,cnt2,cnt3]  
        final=[]
    for i in range(len(lst)):
        if lst[i] == max(lst):
            final.append(i+1)
    return (final)
