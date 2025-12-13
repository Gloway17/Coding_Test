def solution(s):
    answer = 0
    
    ss = s.split()
    
    i = 0
    while (1):
        if (i > len(ss)-1):
            break
            
        if (ss[i] == 'Z'):
            answer -= int(ss[i-1])
        else:
            answer += int(ss[i])
        i += 1
            
    return answer