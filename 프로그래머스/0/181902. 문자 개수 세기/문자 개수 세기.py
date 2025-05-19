def solution(my_string):
    answer = []
    
    for c in range(ord('A'), ord('Z')+1):
        count = 0
        for i in range(len(my_string)):
            if my_string[i] == chr(c):
                count += 1
        answer.append(count)
    
    for c in range(ord('a'), ord('z')+1):
        count = 0
        for i in range(len(my_string)):
            if my_string[i] == chr(c):
                count += 1
        answer.append(count)
        
    return answer