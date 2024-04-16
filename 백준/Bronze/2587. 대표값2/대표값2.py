a=0
box=[]
for _ in range(5):
    i= int(input())
    a=a+i# 갱신
    box.append(i)
mean=a//5
box.sort()
median=box[2]

print(mean)
print(median)