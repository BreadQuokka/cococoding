#입력됐던게 다시 나오면 안됨
n = int(input())
lst = []
for i in range(n):
    lst.append(input())
minus=0
for i in lst:
    box=[i[0]]# ['h']
    for j in range(1,len(i)):#1,2,3,4
        if i[j] in box:
            if i[j]==i[j-1]:
                box.append(i[j])
            else:
                minus+=1
                break
        else:
            box.append(i[j])



print(n-minus)




