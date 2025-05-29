def solution(arr, k):
    answer = []
    
    for n in arr:
        if not n in answer:
            answer.append(n)
        
        if len(answer) == k:
            break
    
    if len(answer) < k:
        while not len(answer) == k:
            answer.append(-1)
    
    return answer