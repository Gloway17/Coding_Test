from collections import Counter

def solution(a, b, c, d):
    l = [a, b, c, d]
    c = Counter(l)
    kl = list(c.keys())
    vl = list(c.values())
    
    if len(c) == 1:
        return 1111 * kl[0]
    
    elif len(c) == 2:
        if 2 in vl:
            p = kl[0]
            q = kl[1]
            return (p + q) * abs(p - q)
        
        elif 3 in vl:
            if c[kl[0]] == 3:
                p = kl[0]
                q = kl[1]
            else:
                p = kl[1]
                q = kl[0]
            return pow((10 * p + q), 2)
    
    elif len(c) == 3:
        if c[kl[0]] == 2:
            q = kl[1]
            r = kl[2]
        elif c[kl[1]] == 2:
            q = kl[0]
            r = kl[2]
        else:
            q = kl[0]
            r = kl[1]
        return q * r
    
    elif len(c) == 4:
        kl.sort()
        return kl[0]
    