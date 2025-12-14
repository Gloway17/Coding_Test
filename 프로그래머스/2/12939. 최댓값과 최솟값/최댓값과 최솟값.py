def solution(s):
    answer = ''
    sl = [int(i) for i in s.split()]
    answer += str(min(sl)) + ' ' + str(max(sl))

    return answer