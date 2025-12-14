def solution(my_string):
    answer = 0
    
    my_list = my_string.split()
    
    op = 1
    for i, n in enumerate(my_list):
        if (n == '+'):
            op = 1
            continue
        elif (n == '-'):
            op = -1
            continue
        else:
            if (op == 1):
                answer += int(n)
            else:
                answer -= int(n)
    
    return answer