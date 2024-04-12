def solution(my_string, is_suffix):
    length= len(is_suffix)
    
    if is_suffix==my_string[(-length):]:
        return 1
    else:
        return 0