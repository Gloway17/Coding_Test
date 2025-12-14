def solution(s):
    answer = True
    
    buf = []
    
    for i, s in enumerate(s):
        buf.append(s)
        
        if (buf[-2:] == ['(', ')']):
            buf.pop()
            buf.pop()
    
    if (len(buf) != 0):
        return False

    return True