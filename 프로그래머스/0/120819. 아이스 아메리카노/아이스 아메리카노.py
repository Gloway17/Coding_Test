def solution(money):
    answer = []
    
    answer.extend([money//5_500, money%5_500])
    
    return answer