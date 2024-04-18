def solution(food):
    result=""
    for i in range(1,len(food)):#4번반복
        a=food[i]//2
        for j in range(a):#3
            result+= str(i)
    reverse= result[::-1]
    result+="0"
    return (result+reverse)
    


# def solution(food):
#     result = ""
#     for i in range(len(food)):
#         a = i // 2
#         for j in range(a + 1):  # i의 절반에 1을 더한 만큼 반복
#             result += str(food[i])
#     return result 