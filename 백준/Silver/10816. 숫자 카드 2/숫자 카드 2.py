from collections import defaultdict
n = int(input())
my_dic =defaultdict(int)
line = input().split()
for i in range(n):
    my_dic[line[i]]+=1
m=int(input())
ans=[]
quize = list(input().split())
for i in quize:
    if i in my_dic:
        ans.append(my_dic[i])
    else:
        ans.append(0)
for i in ans:
    print(i, end=" ")