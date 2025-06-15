def solution(rank, attendance):
    l = [(rank[i], i) for i in range(len(rank)) if attendance[i]]
    
    l.sort()
    
    return 10000 * l[0][1] + 100 * l[1][1] + l[2][1]