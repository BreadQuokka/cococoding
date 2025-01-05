# 256= 분해합 245 = 생성자
n = int(input())
number = list(str(n))
#n +n의 첫자리부터 끝자리까지
box=[]
for i in range(1,n):
    ans = i
    for j in list(str(i)):  # ['2','1','6']
        ans += int(j)
    if ans == n:
        box.append(i)
if len(box)>=1:
    print(min(box))
else:
    print(0)