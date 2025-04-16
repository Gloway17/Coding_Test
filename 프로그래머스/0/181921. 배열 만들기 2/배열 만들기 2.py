def solution(l, r):
    answer = []
    
    for i in range(l, r+1):
        check = True
        
        for ch in str(i):
            if not (ch == '0' or ch == '5'):
                check = False
                break
            else:
                pass
        
        if check:
            answer.append(i)
            
    if len(answer) == 0:
        return [-1]
        
    answer.sort()
    return answer