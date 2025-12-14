def solution(emergency):
    answer = [0] * len(emergency)
    ee = emergency[:]
    ee.sort()
    ee = ee[::-1]
    
    answer = [ee.index(i)+1 for i in emergency]
    
    return answer