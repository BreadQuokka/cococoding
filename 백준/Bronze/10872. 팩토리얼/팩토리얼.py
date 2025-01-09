n = int(input())
if n !=0:
    mid =n
    for  i in range(n-1,0,-1):#10 9 8
        # print(mid,"*",i)
        mid = mid*i
    print(mid)
else:
    print(1)

