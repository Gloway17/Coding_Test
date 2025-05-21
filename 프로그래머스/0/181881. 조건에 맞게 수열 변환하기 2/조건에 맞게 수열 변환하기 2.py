import copy

def solution(arr):
    answer = 0
    
    while (True):
        last_arr = copy.deepcopy(arr)
        
        for i in range(len(arr)):
            if arr[i] >= 50 and arr[i] % 2 == 0:
                arr[i] /= 2
            elif arr[i] < 50 and arr[i] % 2 == 1:
                arr[i] = arr[i] * 2 + 1
            else:
                pass
        
        answer += 1
        
        if last_arr == arr:
            return answer - 1