from collections import defaultdict
n,m = map(int, input().split())
ma = n
lst = []
for i in range(n):
    lst.append(input())
#ATGC
ans=[]
num=0
for col in range(m):
    cnt =0
    cash=[]
    my_dic=defaultdict(int)
    for row in range(n):
        my_dic[lst[row][col]]+=1
    max_key =max(my_dic, key=my_dic.get)
    for i in my_dic:
        if my_dic[i]==my_dic[max_key]:
            cash.append(i)
            cnt+=1
    if cnt==1:
        ans.append(max_key)
        # 수
        num+=(ma-my_dic[max_key])
    else:
        cash.sort()
        ans.append(cash[0])
        #수
        num+=(ma-my_dic[max_key])

print("".join(ans))
print(num)
