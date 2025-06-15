def solution(picture, k):
    answer = []
    
    for p in picture:
        row = ""
        for i in range(len(p)):
            row += p[i]*k
        for i in range(k):
            answer.append(row)
    
    return answer