def solution(array):
    answer = 0
    
    idx = 0
    for a in range(len(array)):
        if (array.count(array[a]) >= array.count(array[idx])):
            idx = a
    
    for a in range(len(array)):
        if (array[a] != array[idx]):
            if (array.count(array[a]) == array.count(array[idx])):
                return -1
    
    return array[idx]