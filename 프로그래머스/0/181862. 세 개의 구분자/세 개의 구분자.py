def solution(myStr):
    tmp = []
    
    tmp = myStr.replace('b', 'a').replace('c', 'a').split('a')
    
    answer = []
    for s in tmp:
        if not s == '':
            answer.append(s)
    
    if answer == []:
        return ["EMPTY"]
    
    return answer