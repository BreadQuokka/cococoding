def solution(sides):
    #n이 (큰-작)보다 크고 (큰+작)보다 작아야함
    count=0
    for i in range (sum(sides)+1):
        if (max(sides)-min(sides))< i < sum(sides):
            count+=1
    return count