def solution(arr1, arr2):
    long= len(arr1[0])
    final=[]
    for i in range (len(arr1)):
        box=[]
        for j in range(long):#만약 1이라면?
            ans= arr1[i][j]+arr2[i][j]
            box.append(ans)
        final.append(box)
    return final

            
            