def solution(arr, flag):
    answer = []
    
    for i in range(len(flag)):
        if flag[i]:
            answer.extend([arr[i]]*2*arr[i])
        else:
            answer = answer[:-arr[i]]
    
    return answer