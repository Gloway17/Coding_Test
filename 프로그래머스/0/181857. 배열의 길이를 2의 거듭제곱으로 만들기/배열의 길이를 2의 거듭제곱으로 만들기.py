def solution(arr):
    answer = []
    
    target_len = 1
    while True:
        if len(arr) <= target_len:
            break
        target_len *= 2
        
    for i in range(target_len):
        if i < len(arr):
            answer.append(arr[i])
        else:
            answer.append(0)
    
    return answer