def solution(my_string):
    answer = ''
    
    for i, c in enumerate(my_string):
        if (c.isupper()):
            answer += c.lower()
        else:
            answer += c.upper()
    
    return answer