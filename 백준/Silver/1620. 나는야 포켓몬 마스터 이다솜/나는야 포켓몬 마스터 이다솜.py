n, q = map(int, input().split())
my_dic ={}
my_dic2={}

for i in range(1,n+1):
    a = input()
    my_dic[a] = i
    my_dic2[i] = a

quize=[]
for i in range(q):
    quize.append(input())
ans=[]
for i in quize:
    try:
        i =int(i)
        ans.append(my_dic2[i])
    except:
        ans.append(my_dic[i])

for i in ans:
    print(i)