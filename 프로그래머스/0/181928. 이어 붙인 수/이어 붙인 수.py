def solution(num_list):
    answer = 0
    
    odd_n = ''
    even_n = ''
    
    for i in num_list:
        if i % 2:
            odd_n += str(i)
        else:
            even_n += str(i)
    
    answer = int(odd_n) + int(even_n)
    
    return answer