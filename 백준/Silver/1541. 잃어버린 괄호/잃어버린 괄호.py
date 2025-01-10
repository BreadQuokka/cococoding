str =input()
#50-40+30+10
ans=""
box=[]
noo=[]
middle=0
for i in str:
    if i!="-":
        ans+=i
    else:
        noo = list(map(int,ans.split("+")))
        middle = sum(noo)
        box.append(middle)
        ans=""
        noo=[]
box.append(sum(list(map(int,ans.split("+")))))
ans=box[0]
for i in box[1:]:#[50, 80, 60]
    ans-=i
print(ans)
