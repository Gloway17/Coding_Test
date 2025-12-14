def solution(id_pw, db):
    answer = ''
    
    if id_pw in db:
        return "login"
    
    for i, n in enumerate(db):
        if (n[0] == id_pw[0]):
            if (n[1] != id_pw[1]):
                return "wrong pw"
    return "fail"