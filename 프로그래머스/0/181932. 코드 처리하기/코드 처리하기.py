def solution(code):
    ret = ''
    mode = 0
    
    for idx in range(len(code)):
        if code[idx] == '1':
            mode = (mode + 1) % 2
        else:
            if not mode:
                if not idx % 2:
                    ret += code[idx]
            else:
                if idx % 2:
                    ret += code[idx]
        
    if ret == '':
        return 'EMPTY'
    return ret