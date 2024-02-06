a= input()
L=len(a)//2
count=0
for i in range (L):
    if a[i] ==a[(-i-1)]:
        count+=1
        continue  
    else:
        break

if count==L:
    print(1)
else:
    print(0)
