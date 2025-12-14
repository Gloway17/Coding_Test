def solution(keyinput, board):
    answer = [0, 0]
    tmp = [0, 0]
    button = {'up':[0,1], 'down':[0,-1], 'left':[-1,0], 'right':[1,0]}
    
    w_border = (board[0]-1)//2
    h_border = (board[1]-1)//2
    
    for i, k in enumerate(keyinput):
        tmp = answer[:]
        tmp[0] += button[k][0]
        tmp[1] += button[k][1]
        
        if ( (w_border*-1 <= tmp[0] and tmp[0] <= w_border) and
               (h_border*-1 <= tmp[1] and tmp[1] <= h_border) ):
            answer = tmp[:]
        else:
            continue
            
    return answer