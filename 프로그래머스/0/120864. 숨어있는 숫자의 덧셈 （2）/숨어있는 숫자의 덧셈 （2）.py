def solution(my_string):
    answer = 0
    
    buf = ''
    for c in my_string:
        if (c.isdigit()):
            buf += c
        else:
            if (buf):
                answer += int(buf)
                buf = ''
    if (buf):
            answer += int(buf)
            buf = ''
    return answer