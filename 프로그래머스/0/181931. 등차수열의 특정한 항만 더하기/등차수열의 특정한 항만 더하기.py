def solution(a, d, included):
    answer = 0
    
    for i in range(len(included)):
        if included[i]:
            n = a + i * d
            answer += n
        
    return answer