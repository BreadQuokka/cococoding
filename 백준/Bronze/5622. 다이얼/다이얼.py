abc= "abcdefghijklmnopqrstuvwxyz".upper()
str = input()
box=[]
for i in str:
    if i in abc[:3]:
        box.append(3)
    if i in abc[3:6]:
        box.append(4)
    if i in abc[6:9]:
        box.append(5)# 다이얼4
    if i in abc[9:12]:
        box.append(6)
    if i in abc[12:15]:
        box.append(7)
    if i in abc[15:19]:
        box.append(8)
    if i in abc[19:22]:
        box.append(9)
    if i in abc[22:]:
        box.append(10)
print(sum(box))



