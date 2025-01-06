n = int(input())

for i in range(n):
    ans=""
    line = input().split()
    times= int(line[0])
    quest = line[1]
    for i in quest:
        ans+=i*times
    print(ans)
