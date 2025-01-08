n = input()
box=[]
for i in n:
    box.append(i)
box.sort(reverse = True)
for i in box:
    print(i,end="")