def solution(strArr):
    answer = 0
    count = [0] * 31
    
    for s in strArr:
        count[len(s)] += 1
    
    answer = max(count)
    
    return answer