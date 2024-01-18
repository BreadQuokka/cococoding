def solution(money):
    a={"잔수":0,"나머지":0}
    a["잔수"]=money//5500
    a["나머지"]=money%5500
    return list(a.values())