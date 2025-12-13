def solution(age):
    answer = ''
    
    s = 'abcdefghij'
    
    for c in str(age):
        answer += s[int(c)]
    
    return answer