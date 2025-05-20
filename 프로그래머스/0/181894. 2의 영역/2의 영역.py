def solution(arr):
    answer = []
    
    if not 2 in arr:
        return [-1]
    
    idx_arr = []
    try:
        tmp = 0
        while (True):
            idx_arr.append(arr.index(2, tmp))
            tmp = arr.index(2, tmp) + 1
    except:
        answer.extend(arr[idx_arr[0]:idx_arr[-1]+1])
        
    return answer