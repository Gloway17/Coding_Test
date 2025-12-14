def solution(A,B):
    answer = 0

    A.sort()
    B.sort()
    
    for i, n in enumerate(A):
        answer += A[i] * B[len(B)-1-i]

    return answer