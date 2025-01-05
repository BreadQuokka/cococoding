#아는 단어 집합을 만들어.-> 거기 있으면 그 단어 카운트 높여 -> 젤 높은 카운트
n = int(input())
lst=[]
for i in range(n):
    line = input().replace(" ","")
    lst.append(line)
ans =[]
for i in lst:
    my_dic = {}
    for j in i:
        if j not in my_dic:
            my_dic[j] = 1
        else:
            my_dic[j] += 1
    maxval = max(my_dic.values())
    count=0
    for key,value in my_dic.items():
        if value==maxval:
            count+=1
            max_key = key
    if count==1:
        ans.append(max_key)
    else:
        ans.append("?")


for i in ans:
    print(i)





