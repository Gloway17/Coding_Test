def solution(n, control):
    answer = 0
    
    for ch in control:
        if ch == 'w':
            n += 1
            pass
        elif ch == 's':
            n -= 1
            pass
        elif ch == 'd':
            n += 10
            pass
        elif ch == 'a':
            n -= 10
            pass
    
    return n