n = input()
have = set(map(int,input().split()))
new_n = int(input())
guess = list(map(int,input().split()))
box=[]
for i in guess:
    if i in have:
        box.append(1)
    else:
        box.append(0)
print(" ".join(map(str,box)))