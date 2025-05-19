def solution(my_string, m, c):
    answer = ''
    i = 0
    while (i < len(my_string)):
        answer += my_string[i+c-1]
        i += m
    return answer