def solution(num_list):
    answer=[]
    A= sorted(num_list)
    for i in range(5):
        answer.append(A.pop(0))
    return answer