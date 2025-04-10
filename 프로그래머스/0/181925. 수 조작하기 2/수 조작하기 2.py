def solution(numLog):
    answer = ''
    
    for i in range(len(numLog)-1):
        calc = numLog[i+1] - numLog[i]
        
        if calc == 1:
            answer += 'w'
        elif calc == -1:
            answer += 's'
        elif calc == 10:
            answer += 'd'
        elif calc == -10:
            answer += 'a'
        
    return answer