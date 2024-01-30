def solution(arr, divisor):
    box=[]
    while arr:
        a=arr.pop()
        if a%divisor ==0:
            box.append(a)
    box1=sorted(box)
    if not box:
        return [-1]
    else:
        return box1