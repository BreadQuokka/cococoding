def solution(num_list):
    cop= num_list.copy()
    box= []
    while num_list:
        box.append(num_list.pop())
    return box
    