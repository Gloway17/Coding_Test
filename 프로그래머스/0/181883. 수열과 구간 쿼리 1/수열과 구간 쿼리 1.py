def solution(arr, queries):
    answer = arr[:]
    
    for query in queries:
        s = query[0]
        e = query[1]
        
        for i in range(len(arr)):
            if (s <= i) and (i <= e):
                answer[i] += 1
    
    return answer