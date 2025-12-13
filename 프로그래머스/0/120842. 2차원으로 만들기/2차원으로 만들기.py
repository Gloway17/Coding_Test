def solution(num_list, n):
    answer = []
    
    tmp = []
    for idx, num in enumerate(num_list):
        tmp.append(num)
        if ((idx + 1) % n == 0):
            answer.append(tmp)
            tmp = []
    
    return answer