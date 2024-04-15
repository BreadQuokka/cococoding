s= input()
s= s.upper()
new_s=list(set(s))
box=[]

for i in new_s:
    a=s.count(i)
    box.append(a)
if box.count(max(box))>=2:
    print("?")
else:#h,a,p,y
    print(new_s[box.index(max(box))])