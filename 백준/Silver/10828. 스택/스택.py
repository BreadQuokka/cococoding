n= int(input())
box=[]

for i in range(n):
    a=input()
    if "push" in a:
        box.append(int(a.split()[-1]))
    elif "pop"in a:
        if not box:
            print(-1)
        else: 
            b= box.pop()
            print(b)
    elif "size"in a:
        print(len(box))
    elif "empty" in a:
        if not box:
            print(1)
        else:
            print(0)
    elif "top"in a:
        if not box:
            print(-1)
        else:
            print(box[-1])
        
    