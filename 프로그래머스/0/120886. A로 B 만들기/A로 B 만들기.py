def solution(before, after):
    answer = 1
    
    for c in before:
        if (before.count(c) != after.count(c)):
            return 0
    return answer