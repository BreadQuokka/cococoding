n, m = map(int, input().split())
lst1 = set(map(int,input().split()))
lst2 = set(map(int,input().split()))
left = lst1-lst2
right = lst2-lst1
ans = left|right
print(len(ans))
