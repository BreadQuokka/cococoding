box=[]
for i in range(5):
    line = list(input())
    box.append(line)
str=""
long=0
for i in box:
    if len(i)>long:
        long=len(i)
for i in box:
    if len(i)<long:
        times = long-len(i)
        for j in range(times):
            i.append("@")

for i in range(long):
    for j in range(len(box)):
       str+= box[j][i]

print(str.replace("@",""))