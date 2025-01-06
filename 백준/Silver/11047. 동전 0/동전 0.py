n, total = map(int, input().split())
type =[]
for i in range(n):
    a=int(input())
    if a<=total:
        type.append(a)

count =0
mid = 0
type.sort(reverse=True)
for i in type:
    count+=total//i
    total%= i

print(count)
