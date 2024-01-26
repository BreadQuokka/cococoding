def solution(n):
    box = []

    if n % 2 != 0:
        for i in range(1, n + 1):
            if i % 2 != 0:
                box.append(i)
        return sum(box)
    
    elif n % 2 == 0:
        for i in range(1, n + 1):
            if i % 2 == 0:
                box.append(i**2)
        return sum(box)

   