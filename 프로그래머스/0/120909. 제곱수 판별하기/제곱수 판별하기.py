import math

def solution(n):
    answer = 2
    
    if (math.sqrt(n) == int(math.sqrt(n))):
        answer = 1
    
    return answer