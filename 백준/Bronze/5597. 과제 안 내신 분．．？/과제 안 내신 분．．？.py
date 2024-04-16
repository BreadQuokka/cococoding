arr=[i for i in range(1,31,1)]
box=[]
for i in range(28):
    a=input()
    box.append(int(a))
    
for j in box:
    if j in arr:
        arr.pop(arr.index(j))
print(min(arr))
print(max(arr))