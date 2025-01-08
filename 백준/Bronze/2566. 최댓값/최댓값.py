row =[]
for i in range(9):
    row.append(list(map(int, input().split())))
rr=1

max=0
for i in row:
    for j in i:
        if j>max:
            max =j
# #90 찾기
# for i in row:
#     col = 0
#     for j in i:
#         col+=1
#         if j==max:
#             break
#     rr+=1
# pos =[rr,col]
# print(max, pos)
a=0
for i in row:
    try:
        a = i.index(max)+1
        break
    except:
        rr+=1
        pass
print(max)
print(rr, a)