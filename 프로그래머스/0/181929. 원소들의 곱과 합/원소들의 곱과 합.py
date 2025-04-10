def solution(num_list):
    answer = 0
    
    mul_all = 1
    for i in num_list:
        mul_all *= i
        
    sum_all_pow = sum(num_list)**2
    
    if mul_all < sum_all_pow:
        return 1
        
    return answer