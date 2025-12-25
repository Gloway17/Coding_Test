def solution(spell, dic):
    answer = 2
    
    for i, d in enumerate(dic):
        if (len(d) != len(spell)):
            continue
            
        for j, s in enumerate(spell):
            if (len(d) == 0):
                break
                
            idx = d.find(s)
            if (idx != -1):
                d = d[:idx] + d[idx+1:]
        
        if (len(d) == 0):
            return 1
            
    return answer