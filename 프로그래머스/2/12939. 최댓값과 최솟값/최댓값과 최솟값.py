def solution(s):
    a= s.split()
    b=list(map(int, a))
    answer = f"{min(b)} {max(b)}"
    return answer