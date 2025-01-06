s = input()
string = "abcdefghijklmnopqrstuvwxyz"
ans=[]
for i in string:
    if i in s:
        ans.append(s.find(i))
    else:
        ans.append(-1)
for i in ans:
    print(i, end=" ")
