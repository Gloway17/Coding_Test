def solution(s):
    answer = ''
        
    for i, c in enumerate(s):
        if (i == 0):
            if (c.isdigit()):
                answer += c
            elif (c.isalpha()):
                answer += c.upper()
            continue
        else:
            if (s[i-1] == ' ' and c.isalpha()):
                answer += c.upper()
            elif (c.isalpha()):
                answer += c.lower()
            else:
                answer += c
    
    return answer