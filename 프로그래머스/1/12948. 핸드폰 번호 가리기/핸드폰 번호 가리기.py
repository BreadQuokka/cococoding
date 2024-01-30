def solution(phone_number):
    a=phone_number.replace(phone_number[:-4],'*'*(len(phone_number)-4))
    return a
    
    