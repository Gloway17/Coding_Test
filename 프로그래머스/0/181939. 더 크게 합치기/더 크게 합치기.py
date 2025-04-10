def calc(x, y):
    return int(str(x)+str(y))

def solution(a, b):
    answer = 0
    
    if calc(a, b) > calc(b, a):
        answer = calc(a, b)
    else:
        answer = calc(b, a)
    
    return answer