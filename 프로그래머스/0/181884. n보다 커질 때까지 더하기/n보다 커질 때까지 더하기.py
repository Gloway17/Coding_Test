def solution(numbers, n):
    answer = 0
    
    i = 0
    while not (answer > n):
        answer += numbers[i]
        i += 1
    
    return answer