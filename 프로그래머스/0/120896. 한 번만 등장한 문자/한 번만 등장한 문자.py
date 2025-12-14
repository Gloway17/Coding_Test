def solution(s):
    answer = ''
    
    string = ''
    for c in s:
        if (s.count(c) == 1):
            string += c
    
    string = list(string)
    string.sort()
    
    return ''.join(string)