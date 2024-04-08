def solution(d, budget):
    d.sort()
    sm = 0
    count = 0
    while d and budget >= sm + d[0]:
        sm += d.pop(0)
        count += 1
    return count