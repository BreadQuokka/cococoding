soo ="666"
ans=[]
no=666
while len(ans)<10000:
    if soo in str(no):
        ans.append(no)
    no+=1
n =int(input())
print(ans[n-1])

