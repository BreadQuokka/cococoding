def solution(arr):
    box=[arr[0]]
    for i in range(len(arr)-1):
        if arr[i]!=arr[i+1]:
            box.append(arr[i+1])
    return box
        