import sys
input = sys.stdin.readline
stack=[]
ans=[]
time=int(input())

for i in range(time):
    item = input().split()
    if len(item)==2:#['1','3']
        stack.append(item[1])
    else:
        if item==['2']:
            if stack != []:
                ans.append(stack[-1])
                stack.pop()

            else:
                ans.append(-1)
        if item==['3']:
            ans.append(len(stack))
        if item==['4']:
            if stack != []:
                ans.append(0)
            else:
                ans.append(1)
        if item==['5']:
            if stack != []:
                ans.append(stack[-1])
            else:
                ans.append(-1)
for i in ans:
    print(i)