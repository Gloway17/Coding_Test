def solution(quiz):
    answer = [''] * len(quiz)
    
    result = 0
    for i, qq in enumerate(quiz):
        qqq = qq.split()
        if (qqq[1] == '+'):
            result = int(qqq[0]) + int(qqq[2])
        else:
            result = int(qqq[0]) - int(qqq[2])
        
        if (result == int(qqq[4])):
            answer[i] = "O"
        else:
            answer[i] = "X"
    
    return answer