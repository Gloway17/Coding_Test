import math

def solution(array, n):
    array.sort()
    diff = [abs(i-n) for i in array]
    
    return array[diff.index(min(diff))]