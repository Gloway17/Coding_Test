def solution(numbers):
    answer = 0

    numbers.sort()
    
    num1 = numbers[-1]*numbers[-2]
    num2 = numbers[0]*numbers[1]
    
    return num1 if num1 > num2 else num2