def solution(my_string):
    a=my_string.swapcase()
    return a



# string은 덧셈이 된다


def solution(my_string):
    answer = ''

    for i in my_string:
        if i.isupper():
            answer+=i.lower()
        else:
            answer+=i.upper()
    return answer