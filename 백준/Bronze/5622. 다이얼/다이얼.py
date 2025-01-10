abc = "abcdefghijklmnopqrstuvwxyz".upper()
str = input()
box = []

for i in str:
    if i in abc[:3]:       # ABC
        box.append(3)
    elif i in abc[3:6]:    # DEF
        box.append(4)
    elif i in abc[6:9]:    # GHI
        box.append(5)
    elif i in abc[9:12]:   # JKL
        box.append(6)
    elif i in abc[12:15]:  # MNO
        box.append(7)
    elif i in abc[15:19]:  # PQRS
        box.append(8)
    elif i in abc[19:22]:  # TUV
        box.append(9)
    elif i in abc[22:]:    # WXYZ
        box.append(10)

print(sum(box))