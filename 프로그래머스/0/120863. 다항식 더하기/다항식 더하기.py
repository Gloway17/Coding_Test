def solution(polynomial):
    answer = ''
    pp = polynomial.split()
    
    x_n = 0
    n_n = 0
    for i, p in enumerate(pp):
        if (p == '+'):
            continue
        if 'x' in p:
            if (p[:-1]==''):
                x_n += 1
            else:
                x_n += int(p[:-1])
        else:
            n_n += int(p)
            
    if (x_n == 0):
        pass
    elif (x_n == 1):
        answer += 'x'
    else:
        answer += str(x_n)+'x'
        
    if (n_n == 0):
        pass
    else:
        if (answer):
            answer += ' + '+str(n_n)
        else:
            answer += str(n_n)
    
    return answer