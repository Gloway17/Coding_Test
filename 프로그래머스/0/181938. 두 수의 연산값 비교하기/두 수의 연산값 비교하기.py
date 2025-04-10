def solution(a, b):
    answer = 0
    
    c1 = int(str(a) + str(b))
    c2 = 2 * a * b
    
    if c1 >= c2:
        answer = c1
    else:
        answer = c2
    
    return answer