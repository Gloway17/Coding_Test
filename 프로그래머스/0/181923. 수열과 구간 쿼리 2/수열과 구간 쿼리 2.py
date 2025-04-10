def solution(arr, queries):
    answer = []
    
    for query in queries:
        s = query[0]
        e = query[1]
        k = query[2]
        
        min = 1_000_000
        
        for i in range(len(arr)):
            if i >= s  and i <= e:
                if arr[i] > k:
                    if arr[i] < min:
                        min = arr[i]
        if min == 1_000_000:
            min = -1
            
        answer.append(min)
        
    return answer