def solution(arr):
    if len(arr)>len(arr[0]): # 행의 수가 더 많은 경우
        length= len(arr)-len(arr[0])
        for i in arr:
            for j in range(length):
                i.append(0)
        return arr
    
    elif len(arr)<len(arr[0]):
        box=[]
        length= len(arr[0])-len(arr)
        for j in range(len(arr[0])):
            box.append(0)
        for i in range(length):
            arr.append(box)
        return arr

    
    else:
        return arr