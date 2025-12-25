def solution(n):
    answer = []
    
    d = 2
    while (n != 1):
        if (n % d == 0):
            n = n // d
            answer.append(d)
        else:
            d += 1
    
    answer = list(set(answer))
    
    answer.sort()
    
    return answer