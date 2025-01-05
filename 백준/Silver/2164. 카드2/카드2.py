from collections import deque
n = int(input())
qqq = deque()
for i in range(1,n+1):
    qqq.append(i) # 1234

while len(qqq) != 1:
    qqq.popleft()
    block = qqq.popleft()
    qqq.append(block)
print(qqq[0])