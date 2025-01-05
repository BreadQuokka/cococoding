from collections import deque
ans=[]
n = int(input())
qqq= deque()
for i in range(n):
    con = input()
    if "push" in con:
        qqq.append(con.split()[-1])
    if con =="pop":
        try:
            ans.append(qqq[0])
            qqq.popleft()
        except:
            ans.append(-1)
    if con =="size":
        ans.append(len(qqq))
    if con =="empty":
        if len(qqq) == 0:
            ans.append(1)
        else:
            ans.append(0)
    if con =="front":
        try:
            ans.append(qqq[0])
        except:
            ans.append(-1)
    if con =="back":
        try:
            ans.append(qqq[-1])
        except:
            ans.append(-1)
for i in ans:
    print(i)