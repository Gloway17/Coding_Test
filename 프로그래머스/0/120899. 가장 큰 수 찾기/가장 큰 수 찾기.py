def solution(array):
    answer = [-1, -1]
    
    for idx, num in enumerate(array):
        if (answer[0] < num):
            answer = [num, idx]
    
    return answer